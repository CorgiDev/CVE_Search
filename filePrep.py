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
    try:
        with open(oldFilePath) as oldfile, open(newFilePath, 'w', encoding='utf-8') as newfile:
            for line in oldfile:
                if not any(badword in line for badword in badwords):
                    newfile.write(line)
    except UnicodeDecodeError as err:
        print('Weird error, "', err, '" occurred.')
    # Remove old file
    deleteFile(fileDir, fileName)
    # Rename new file to old filename
    renameFile(fileDir, newFileName, fileName)
    print("Search data format complete.")