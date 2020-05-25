#import
import os, shutil, requests, sys, csv

####################
# Defined Functions
####################
# Download File
def downloadFile(url, fileName, full_Dir):
    r = requests.get(url)
    # Set some diagnostic values
    statusCode = r.status_code
    #contentType=r.headers['content-type']
    #encoding=r.encoding
    # Begin saving file
    with open(full_Dir, 'wb') as f:
        f.write(r.content)
    # Check if status code error
    statusCodeCheck(fileName, statusCode)

# Prep file for import
def fileFormat(fileDir, filename, badwords):
    oldFilePath = fileDir + filename
    newFilePath = fileDir + "New_" + filename
    # Check if a line in the old file contains an invalid phrase.
    # If not, add it to a new copy of the file.
    with open(oldFilePath) as oldfile, open(newFilePath, 'w') as newfile:
        for line in oldfile:
            if not any(badword in line for badword in badwords):
                newfile.write(line)

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

# Check Status Code from HTTP Request
def statusCodeCheck(fileName, statusCode):
    if statusCode in range(100, 300):
        print("Updated", fileName, "downloaded successfully.")
    elif statusCode in range (300, 400):
        print("Updated", fileName, "download unsuccessful due to ", statusCode, ": Redirect Error")
    elif statusCode in range (400, 500):
        print("Updated", fileName, "download unsuccessful due to ", statusCode, ": Client Error, which is usually due to file not found or access forbidden.")
    elif statusCode in range (500, 600):
        print("Updated", fileName, "download unsuccessful due to ", statusCode, ": Server Error, maybe the site is down.")
    else:
        print("Sorry the error is unknown. Try again later.")