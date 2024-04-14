#!/usr/bin/env python
from shared.libraries import argparse, requests, exit, mmh3, md5, os,codecs
from shared.lookup import mmh3Lookup, md5Lookup
from concurrent.futures import ThreadPoolExecutor
from shared.common import displayBanner, update, checkFiles, generateCommands, defaultFilename,colored
import tldextract
import shodan
from tqdm import tqdm
import subprocess
import threading
# Store target details
class Server:
    def __init__(self, url=None, port=None):
        if url is None:
            self.url = "http://localhost"  # Set a default URL if None
        else:
            self.url = url if url.startswith('http://') or url.startswith('https://') else "http://" + url
        self.port = port if port is not None else port
        self.target = self.url + ':' + self.port if port is not None else self.url
        self.mmh3 = self.mmh3Hash()
        self.md5 = self.md5Hash()

    def __call__(self):
        print("Provide a valid URL")

    def fetch_favicon(self):
        favicon = "/favicon.ico"  # Default favicon path, consider updating this based on common paths
        url = self.target if self.target.endswith((".ico", ".svg", ".jpg", ".png", ".jpeg")) else self.target + "/" + favicon
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            pass
            return None

    def md5Hash(self):
        favicon_data = self.fetch_favicon()
        if favicon_data:
            return md5(favicon_data).hexdigest()
        else:
            return None

    def mmh3Hash(self):
        favicon_data = self.fetch_favicon()
        if favicon_data:
            favicon = codecs.encode(favicon_data, 'base64')
            hash_val = mmh3.hash(favicon)
            return hash_val
        else:
            return None
        
def processURL(line):
    try:
        if not line.strip():
            return
        with open(f'{os.getcwd()}/{defaultFilename}', 'a') as file:
            data = Server(url=line.strip(), port=None)
            if (data.md5!=None or data.mmh3 !=None):
                file.write(f"{data.target},{data.mmh3},{data.md5}")
            file.write("\n")
    except Exception as e:
        # Write errors to a separate file
        print(f"Error Writing Files : {e}")

def selfUpdate():
    try:
        mainLocation = os.path.dirname(os.path.realpath(__file__))

        def threadUpdate():
            os.chdir(mainLocation)
            gitPullCommand = ["git", "pull"]
            try:
                subprocess.run(gitPullCommand, check=True)
                print("Update successful.")
            except subprocess.CalledProcessError as e:
                print(f"Error during Git pull: {e}")

        gitPullThread = threading.Thread(target=threadUpdate)
        gitPullThread.start()
        gitPullThread.join()  # Wait for the thread to finish before continuing

    except Exception as ex:
        print(f"An error occurred during the update process: {ex}")
        
def captureIPs(inputString=None,hash=None,output=None,apiKey=None) -> None:
    def checkURL(input) -> bool:
        if str(input).startswith("https://") or str(input).startswith("http://"):
            return True
        else:
            return False
    
    if inputString is None or hash is None or apiKey is None:
        print("Requires 2 Parameters for this operation eg : --url https://google.com --hash 708578229 --apiKey $SHODAN_API")
        exit(0)
    
    domain=inputString if checkURL(input=inputString) is False else f"{tldextract.extract(inputString).domain}.{tldextract.extract(inputString).suffix}"
    hashLookup=str(hash)
    
    api=shodan.Shodan(apiKey)
    try:
        print(f"🔥 Capturing  IPs.. -> {domain}")
        query=f'org:"{domain}" http.favicon.hash:{hashLookup}'
        results = api.search(query, facets={'ip_str': None, 'port': None})
        ipPortLists = [f"{result['ip_str']}:{result['port']}" for result in results['matches']]
        
        # Writing the results to a file
        
        filename =output if output is not None else f"{domain}_{hashLookup}.txt" 
        with open(filename, 'w') as f:
            for ip_port in ipPortLists:
                f.write(ip_port + '\n')

        print(f"🍲 Saving as\t\t: {colored(f'{os.getcwd()}/{filename}','yellow')}")

    except shodan.APIError as e:
        print(f"😞 Error: {e}")
    except Exception as e:
        print(f"😞 Error Looking Up IP's : {e}")
    except KeyboardInterrupt:
        exit(0)
    
        
# Entry Point
if __name__ == "__main__":
    try:
        parser=argparse.ArgumentParser(description="Reconfavicon - investigate favicons, lookup associated products and generate lookup comands")
        parser.add_argument("--url","-u",dest="url",required=False,help="Server URL or IP, eg : http://example.com")
        parser.add_argument("--port","-p",dest="port",required=False,help="Server Port, eg: 8080")
        parser.add_argument("--no-banner","-n",action="store_true",required=False,help="Prevents the Banner from loading")
        parser.add_argument("--file","-f",dest="urllists",required=False,help="File containing list of urls, fetches only hashes, will ignore other switches")
        parser.add_argument("--threads","-t",dest="threads",required=False,help="Used with -f switch, will ignore other switches # (Default 20 Threads)")
        parser.add_argument("--update","-up",action="store_true",required=False,help="Update Lookup Table")
        parser.add_argument("--hash",dest="hash",required=False,help="Capture All IP addresses associated with an organisation's favicon hash")
        parser.add_argument("--output","-o",dest="output",help="Filename for saving results",required=False)
        parser.add_argument("--apiKey",dest="apiKey",help="Shodan API Key or Environment Variable containing Shodan API Key")
        args=parser.parse_args()
        # Check if the dataset exist
        checkFiles()
        if not args.no_banner:
            displayBanner()
        if args.update and args.url!=None:
            update()
            selfUpdate()
        if args.hash and args.url:
            if not args.apiKey:
                print(f"😞 Pass the Shodan API Key!")
                exit(0)
            else:
                captureIPs(hash=args.hash,inputString=args.url,output=args.output if args.output else None,apiKey=args.apiKey)
                exit(0)
        elif args.urllists:
                try:
                    if args.threads:
                        threads=args.threads
                    else:
                        threads=20
                    print(f"🍲 Saving as\t\t: {colored(f'{os.getcwd()}/{defaultFilename}','yellow')}")
                    with open(defaultFilename,'w') as file:
                        header=f"URL,MMH3-Hash,MD5-Hash\n"
                        file.write(header)
                    with open(args.urllists, 'r') as file:
                        total_lines = sum(1 for _ in file)
                        file.seek(0)  # Reset file pointer to the beginning
                        
                        with tqdm(total=total_lines, desc=f"🍜 Processing {args.urllists}  ",unit=" URL") as pbar:
                            with ThreadPoolExecutor(max_workers=threads) as executor:
                                for _ in executor.map(processURL, file):
                                    pbar.update(1)
                except Exception as e:
                    print(f"Error getting urls from {args.urllists}: {e}")
                    exit(0)
                except KeyboardInterrupt:
                    exit(0)
                exit(0)
        elif args.update and args.url is None:
            update()
            selfUpdate()
            exit()
        else:
            print("\n")
        target=Server(url=args.url,port=args.port)
        print(colored(f'🎯 Targeting\t\t: {target.target}','red'))
        md5=target.md5
        mmh3=target.mmh3
        if md5 or mmh3:
           print(colored(f'🔑 MD5\t\t\t: {md5}\n🔑 MMH3\t\t\t: {mmh3}','cyan')) if md5 and mmh3 else print(f"🔑 MMH3\t\t\t: {mmh3}") if mmh3 else print(f"🔑 MD5\t\t\t: {md5}")
        else:
            print(colored("No results found, favicon missing/has different path!",'red'))
        # Lookup
        mmh3Lookup(mmh3=mmh3)
        md5Lookup(md5=md5)
        generateCommands(mmh3=mmh3,md5=md5)
        exit(0)
    except KeyboardInterrupt:
        exit(0)
