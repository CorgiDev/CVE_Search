#import
import os, shutil, requests, sys

####################
# Defined Functions
####################
# Download File
def downloadFile(url, fileName, full_Dir):
    r = requests.get(url)
    # Set some diagnostic values
    statusCode = r.status_code
    contentType=r.headers['content-type']
    encoding=r.encoding
    # Begin saving file
    with open(full_Dir, 'wb') as f:
        f.write(r.content)
    # Check if status code error
    is_between = 100 <= int(statusCode) <= 299
    if is_between = True
        print("Updated", fileName, "downloaded successfully.")
    else print("Updated", fileName, "download unsuccessful due to to ", r.status_code)

# Prep file for import
def filePrep():
    print("Hello")

# Import file to dictionary
def fileImport():
    print("Hello")

# Search for item in list by CVE label
def searchByCVEName():
    print("Hello")

# Search for item based on phrase anywhere in the CVE description
def searchByAny():
    print("Hello")

# Consider rewatching the string methods video in Python basics