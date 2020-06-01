#imported modules
import os, shutil, requests, sys, csv

####################
# Defined Functions
####################
# Remove directory
def removeDirectory(dirName):
    print("Removing outdated vulnerability search data.")
    shutil.rmtree(dirName)

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

# OLD FUNCTION, JUST PASTED HERE TO HELP ME FIGURE OUT AN ISSUE
# def downloadFile(url, fileName, full_Dir):
#     r = requests.get(url)
#     # Set some diagnostic values
#     statusCode = r.status_code
#     #contentType=r.headers['content-type']
#     #encoding=r.encoding
#     # Begin saving file
#     with open(full_Dir, 'wb') as f:
#         f.write(r.content)
#     # Check if status code error
#     statusCodeCheck(fileName, statusCode)