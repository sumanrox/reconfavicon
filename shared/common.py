
from .libraries import timedelta,timer,colored,socket,BeautifulSoup,requests,os
from pandas import DataFrame,read_csv,notna,NA
import subprocess
remoteServer='one.one.one.one'
scriptLocation=os.path.dirname(os.path.realpath(__file__))
mainLocation=f"{scriptLocation}/../"
shodanDataset=f"{scriptLocation}/shodan-dataset.csv"
OWASPDataset=f"{scriptLocation}/owasp-dataset.txt"
shodanOnlineData="https://raw.githubusercontent.com/sansatart/scrapts/master/shodan-favicon-hashes.csv"
OWASPOnlineData="https://wiki.owasp.org/index.php/OWASP_favicon_database"
defaultFilename="faviconhashes.csv"


def displayBanner():
    banner="""
    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗███████╗ █████╗ ██╗   ██╗██╗ ██████╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔═══██╗████╗  ██║
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╗  ███████║██║   ██║██║██║     ██║   ██║██╔██╗ ██║
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔══╝  ██╔══██║╚██╗ ██╔╝██║██║     ██║   ██║██║╚██╗██║
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║     ██║  ██║ ╚████╔╝ ██║╚██████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ver.2024                                                                                              
    by Suman Roy | Made with ♥
    """
    print(colored(banner,'red'))

# Check internet connectivity
def Connected(hostname):
    try:
        host=socket.gethostbyname(hostname)
        s=socket.create_connection((host,80),2)
        s.close()
        return True
    except Exception:
        pass
    return False

def cleanNewlines(row):
    favicon_hash = row['http.favicon.hash']
    more_info = row['More Info']

    if notna(favicon_hash) and notna(more_info):
        # Split the 'More Info' column based on the 'http.favicon.hash' value
        lines = str(more_info).split(str(favicon_hash))
        # Concatenate the lines into a single line
        return ' '.join(line.strip() for line in lines)

    return more_info

def cleanQuotes(row):
    # Remove double quotation marks in each cell
    return str(row).replace('"', '')

def optimize(dataset):
        data = read_csv(dataset)
        df = DataFrame(data)

        # Replace '(Blank)' and empty strings with NaN
        df.replace({'(Blank)': NA, '': NA}, inplace=True)

        # Remove rows where 'http.favicon.hash' is the only non-NaN value
        df = df.dropna(subset=['http.favicon.hash'], how='all')

        # Clean up double quotation marks in the entire DataFrame
        df = df.applymap(cleanQuotes)

        # Clean up newlines in 'More Info' column based on 'http.favicon.hash'
        df['More Info'] = df.apply(cleanNewlines, axis=1)

        # Count the number of non-NaN values in each row
        df['non_nan_count'] = df.apply(lambda row: row.notna().sum(), axis=1)

        # Sort the DataFrame based on the number of non-NaN values in descending order
        df = df.sort_values(by=['non_nan_count'], ascending=False).drop(columns=['non_nan_count'])

        # Save the sorted and cleaned DataFrame back to a CSV file
        df.to_csv(dataset, index=False)


# if dataset doesn't exist fetch the files
def fetchFile(url):
    if not Connected(remoteServer):
        print(f"Not Connected to internet!")
        exit(0)
    if url.endswith(".csv"):
        flag=True
    else:
        flag=False
    try:
        response=requests.get(url,stream=flag)
        response.raise_for_status()
        try:
            if url.endswith("csv"):
                with open(f"{shodanDataset}",'wb') as fileWriter:
                    fileWriter.write(response.content)
                    fileWriter.close()
        except Exception as e:
            print(f"Error Fetching Shodan Database {e}")
        else:
            try:
                soup=BeautifulSoup(response.text,'lxml')
                tag=soup.find('pre')
                if tag:
                    dataset=tag.get_text().strip()
                    with open(f"{OWASPDataset}",'w') as fileWriter:
                        fileWriter.write(dataset)
                        fileWriter.close()
            except Exception:
                print("Error Fetching OWASP Database")
    except Exception as e:
        print(f"Error fetching Database {e}")

# Check for dataset
def checkFiles():
    owasp=os.path.isfile(OWASPDataset)
    shodan=os.path.isfile(shodanDataset)
    if shodan and owasp:
        return True
    elif not owasp:
        fetchFile(OWASPOnlineData)
        checkFiles()
    elif not shodan:
        fetchFile(shodanOnlineData)
        optimize(shodanDataset)
        checkFiles()

def update():
    print(colored("✨ Updating...",'green'))
    fetchFile(shodanOnlineData)
    optimize(shodanDataset)
    fetchFile(OWASPOnlineData)
    gitPullCommand = ["git", "pull"]
    gitPullCommand.extend(["-C", mainLocation])
    try:
        subprocess.run(gitPullCommand, check=True)
        print("Git pull completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git pull: {e}")
    
    
def generateCommands(mmh3,md5):
    generate=f"""
🌐 ZoomEye Query [WEB]\t: iconhash:{md5}
🌐 ZoomEye Query [WEB]\t: iconhash:{mmh3}
🌐 Shodan Query  [WEB]\t: http.favicon.hash:{mmh3}
🌐 Shodan Query  [CMD]\t: shodan search http.favicon.hash:{mmh3} --fields ip_str,port --separator
    """
    print(colored(generate,'green')) if mmh3!=None and md5!=None else exit(0)