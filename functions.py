#import
import os, shutil, requests, sys, csv, pandas as pd
#, mpu.pd

####################
# Defined Functions
####################
# Download File
def downloadFile(url, fileName, full_Dir):
    try:
        r = requests.get(url,timeout=3)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    with open(full_Dir, 'wb') as f:
        f.write(r.content)
    print("Download of", fileName, "successful.")
"""     try:
        r = requests.post('somerestapi.com/post-here', data={'birthday': '9/9/3999'})
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print (e.response.text) """

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
def fileImport(fileDir, filename):
    fullFilePath = fileDir + filename
    with open(fullFilePath, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    print(your_list)

def csvImport():
    print("Hello")

# Search for item in list by CVE label
def searchByCVEName():
    print("Hello")

# Search for item based on phrase anywhere in the CVE description
def searchByAny():
    print("Hello")

# Consider rewatching the string methods video in Python basics