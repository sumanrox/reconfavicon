from .libraries import colored
from .common import shodanDataset,OWASPDataset
from pandas import DataFrame,read_csv,notna

def mmh3Lookup(mmh3=None):
    if mmh3 is None:
        return False
    data=read_csv(shodanDataset)
    dataFrame=DataFrame(data)
    result=dataFrame[dataFrame['http.favicon.hash']==mmh3]
    # Check if a matching row is found
    if not result.empty:
        # Extract the first matching row (assuming there's only one match)
        matching_row = result.iloc[0]
        # Print columns that do not have an empty string and do not include the search_value
        for column, value in matching_row.items():
            if value != '' and notna(value):
                if column=="http.favicon.hash":
                    pass
                else:
                    if column=="More Info":
                        print(colored(f"🚀 {column}\t\t: {value}",'magenta'))
                    else:
                        print(colored(f"🚀 {column}\t: {value}",'magenta'))
                        
def md5Lookup(md5=None):
        # Check inside owasp dataset
        if md5 is None:
            return False
        try:
            with open(OWASPDataset,'r') as file:
                for line in file:
                    if md5 in line:
                        info=line.strip().split(':')
                        technology = info[1] if len(info) > 1 else "Unknown"
                        print(colored(f"🚀 Technology\t: {technology}", "magenta"))
                        return True
                else:
                    return False
        except Exception as e:
            print(f"Error Looking up in OWASP Dataset")
            return False