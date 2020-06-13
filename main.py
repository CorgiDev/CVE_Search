#imported modules
import os, shutil

#imported functions
from directoryManagement import removeDirectory
from fileEdit import fileFormat, writeHeader
from extra import gatherInput
from vulnSearch import searchByInput
from dataRefresh import updateSearchData

#variables
cve_URL='https://cve.mitre.org/data/downloads/allitems.csv'
cve_DirName = './CVE_Downloads/'
cve_Filename = 'allitems.csv'
cve_FullPath = cve_DirName + cve_Filename
cve_FileType = '.csv'
lines2Remove = [",,,,,"]
resultFilePath = cve_DirName + 'results.csv'

# Refresh search data
if os.path.exists(cve_DirName):
    removeDirectory(cve_DirName)
    updateSearchData(cve_DirName, cve_URL, cve_Filename, cve_FullPath)
else:
    updateSearchData(cve_DirName, cve_URL, cve_Filename, cve_FullPath)

# Format csv file for use
fileFormat(cve_DirName, cve_Filename, lines2Remove)
# Create the result file
writeHeader(cve_FullPath, resultFilePath)

# Search by keyword
#searchByInput(cve_DirName, cve_Filename)
gatherInput(cve_DirName, cve_Filename, resultFilePath)