#imported modules
import os, shutil

#imported functions
from directoryManagement import removeDirectory
from fileEdit import fileFormat, writeHeader
#from csvSearch import gatherInput
from vulnSearch import searchByInput
from dataRefresh import updateSearchData

#variables
cve_URL='https://cve.mitre.org/data/downloads/allitems.csv'
cve_DirName = './CVE_Downloads/'
cve_Filename = 'allitems.csv'
resultFileName = 'results.csv'
cve_FullPath = cve_DirName + cve_Filename
resultFilePath = cve_DirName + resultFileName
lines2Remove = [",,,,,"]
cve_FileType = '.csv'

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
searchByInput(cve_FullPath, resultFilePath)
#gatherInput(cve_DirName, cve_Filename, resultFilePath)