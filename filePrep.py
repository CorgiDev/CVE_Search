#imported modules
import os, shutil, requests, sys, csv

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