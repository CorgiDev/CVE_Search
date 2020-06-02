#imported modules
import os, shutil, requests, sys, csv
from directoryManagement import deleteFile, renameFile

# Prep file for import
def fileFormat(fileDir, fileName, badwords):
    print("Search data being formatted for import.")
    oldFilePath = fileDir + fileName
    newFileName = "New_" + fileName
    newFilePath = fileDir + newFileName
    # Copy needed lines to new file
    with open(oldFilePath) as oldfile, open(newFilePath, 'w') as newfile:
        for line in oldfile:
            if not any(badword in line for badword in badwords):
                newfile.write(line)
    # Remove old file
    deleteFile(fileDir, fileName)
    # Rename new file to old filename
    renameFile(fileDir, newFileName, fileName)
    print("Search data format complete.")

# Import file to dictionary
""" def fileImport(fileDir, filename):
    fullFilePath = fileDir + filename
    with open(fullFilePath, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    print(your_list) """

def csvImport():
    print("Hello")