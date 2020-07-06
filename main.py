# imported modules
import os
import shutil

# imported functions
from directoryManagement import removeDirectory
from fileEdit import fileFormat, writeHeader
from vulnSearch import searchByInput
from dataRefresh import updateSearchData

# variables
cve_URL = 'https://cve.mitre.org/data/downloads/allitems.csv'
cve_DirName = './CVE_Downloads/'
cve_Filename = 'allitems.csv'
resultFileName = 'results.csv'
cve_FullPath = cve_DirName + cve_Filename
resultFilePath = cve_DirName + resultFileName
lines2Remove = [",,,,,", "** REJECT **", "** RESERVED **"]
cve_FileType = '.csv'

# Refresh search data
if os.path.exists(cve_DirName):
    refreshPrompt = input(
        "Pre-existing data found, would you like to refresh? (this may take a minute to update)\n\tEnter (yes) to refresh, else resume program. $ ")
    if refreshPrompt.lower() == "yes":
        removeDirectory(cve_DirName)
        updateSearchData(cve_DirName, cve_URL, cve_Filename, cve_FullPath)
else:
    updateSearchData(cve_DirName, cve_URL, cve_Filename, cve_FullPath)

# Format search data and result csv files for use
fileFormat(cve_DirName, cve_Filename, lines2Remove)
writeHeader(cve_FullPath, resultFilePath)

# Search by keyword
searchByInput(cve_FullPath, resultFilePath)
