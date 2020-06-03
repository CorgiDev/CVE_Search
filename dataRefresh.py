#imported modules
import os, requests

# Update search data
def updateSearchData(dirName, url, fileName, fullPath):
    print("Obtaining updated vulnerability search data.")
    os.mkdir(dirName)
    downloadFile(url, fileName, fullPath)

# Download File
def downloadFile(url, fileName, full_Dir):
    try: 
        response = requests.get(url,timeout=3) 
        response.raise_for_status()                 # Raise error in case of failure 
        with open(full_Dir, 'wb') as f:
            f.write(response.content)
            print("Download of new search data successful.")
    except requests.exceptions.HTTPError as httpErr: 
        print ("Http Error:",httpErr) 
    except requests.exceptions.ConnectionError as connErr: 
        print ("Error Connecting:",connErr) 
    except requests.exceptions.Timeout as timeOutErr: 
        print ("Timeout Error:",timeOutErr) 
    except requests.exceptions.RequestException as reqErr: 
        print ("Something Else:",reqErr)