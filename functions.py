#import
import os, shutil, requests

# Defined Functions
# Check if folder exist
# Download File
# Prep file for import
# Import file to dictionary
# Search for item in list by CVE label
# Search for item based on phrase anywhere in the CVE description
def filePrep():
    print("Hello")

def obtainFile(url, fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print("Obtaining updated", fileName)
        downloadFile(url, fileName)
    else:
        print("Obtaining updated", fileName)
        downloadFile(url, fileName)

def downloadFile(url, fileName):
    r = requests.get(url)
    with open(fileName, 'wb') as f:
        f.write(r.content)
    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)

    # Consider rewatching the string methods video in Python basics