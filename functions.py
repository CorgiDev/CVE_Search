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
    #contentType=r.headers['content-type']
    #encoding=r.encoding
    # Begin saving file
    with open(full_Dir, 'wb') as f:
        f.write(r.content)
    # Check if status code error
    statusCodeCheck(fileName, statusCode)

# Prep file for import
def filePrep(fullFilePath, lines2Remove):
    #############################################
    # Convert file to list of strings
    file2Edit = open(fullFilePath,"w")
    stringList = file2Edit.readlines()
    file2Edit.close()
    # Edit list to remove all lines that end with lines2Remove
    # Convert the list back into a single string
    file2Edit = open(fullFilePath, "w")
    newFileContents = "".join(stringList)
    file2Edit.write(newFileContents)
    file2Edit.close()

def filePrep2(dir, fileName, badLineIdentifier):
    # Variables needed
    fullFilePath = (dir, fileName)
    newFileName = (dir,"new",fileName)
    # Open file to read it
    a_file = open(fullFilePath, "r")
    # Create a list of the lines in the file and close the file.
    lines = a_file.readlines()
    a_file.close()
    # Create a new file to write the lines to
    new_file = open(newFileName, "w")
    for line in lines:
        if badLineIdentifier not in line:
            new_file.write(line)
    new_file.close()

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