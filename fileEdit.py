#imported modules
import os, sys, csv
from csv import writer
from directoryManagement import deleteFile, renameFile, fullFilePath
from extras import rowCountInt

# Prep file for easier reading
def fileFormat(fileDir, fileName, badwords):
    print("Search data being formatted for use. Removing rejected and reserved vuln labels.")
    oldFilePath = fullFilePath(fileDir, fileName)
    newFileName = "New_" + fileName
    newFilePath = fullFilePath(fileDir, newFileName)
    # Copy needed lines to new file
    try:
        with open(oldFilePath) as oldfile, open(newFilePath, 'w') as newfile:
            for line in oldfile:
                if not any(badword in line for badword in badwords):
                    newfile.write(line)
    except UnicodeDecodeError:
        pass
    # Remove old file
    deleteFile(fileDir, fileName)
    # Rename new file to old filename
    renameFile(fileDir, newFileName, fileName)
    # Tell user data format complete and how many search records there are.
    searchRowCount = rowCountInt(oldFilePath)
    searchRecordCountInt = (searchRowCount - 1)
    searchRecordCount = str(searchRecordCountInt)
    print("Search data format complete. " + searchRecordCount + " records obtained.")

def writeHeader(sourceFile, destinationFile):
    try:
        with open(sourceFile) as searchData, open(destinationFile, 'w', encoding='utf-8') as newResultFile:
                    i = 0
                    for line in searchData:
                        while i == 0:
                            i += 1
                            newResultFile.write(line)         
    except UnicodeDecodeError:
        pass

def appendNewRow(fileName, newRow):
    try:
        # Open file in append mode
        with open(fileName, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(newRow)
    except UnicodeDecodeError:
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
    except UnicodeDecodeError:
        pass