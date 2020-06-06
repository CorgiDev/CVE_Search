#imported modules
import os, sys, csv
from csv import writer
from directoryManagement import deleteFile, renameFile

# Prep file for easier reading
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
        print('Decoding error, "', err, '" occurred. You can safely ignore it.')
        pass
    # Remove old file
    deleteFile(fileDir, fileName)
    # Rename new file to old filename
    renameFile(fileDir, newFileName, fileName)
    print("Search data format complete.")

def appendNewRow(fileName, newRow):
    try:
        # Open file in append mode
        with open(fileName, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(newRow)
    except UnicodeDecodeError as err:
                print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
                pass

def appendNewRowList(fileName, newRowList):
    try:
        # Open file in append mode
        for newRow in newRowList:
            with open(fileName, 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(newRow)
    except UnicodeDecodeError as err:
                print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
                pass

def writeHeader(sourceFile, destinationFile):
    try:
        with open(sourceFile) as searchData, open(destinationFile, 'w', encoding='utf-8') as newResultFile:
                    i = 0
                    for line in searchData:
                        while i == 0:
                            i += 1
                            newResultFile.write(line)
                    newResultFile.close()
                    sourceFile.close()            
    except UnicodeDecodeError as err:
                print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
                pass