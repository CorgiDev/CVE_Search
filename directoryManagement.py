# imported modules
import os
import shutil
import requests
import sys
import csv

# Remove directory


def removeDirectory(dirName):
    print("Removing outdated vulnerability search data.")
    shutil.rmtree(dirName)

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
