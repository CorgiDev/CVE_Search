#imported modules
import os, shutil, requests, sys, csv

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

# Delete file
def deleteFile(fileDir, fileName):
    filePath = fullFilePath(fileDir, fileName)
    os.remove(filePath)

# Rename a file
def renameFile(fileDir, oldFileName, newFileName):
    fullOldFileName = fullFilePath(fileDir, oldFileName)
    fullNewFileName = fullFilePath(fileDir, newFileName)
    os.rename(fullOldFileName, fullNewFileName)

# Create a full file path from a dir and file name
def fullFilePath(fileDir, fileName):
    fullPath = fileDir + fileName
    return fullPath