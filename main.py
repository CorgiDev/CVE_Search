#imported modules
import os, shutil

#imported functions
from directoryManagement import removeDirectory
from filePrep import fileFormat
from vulnSearch import searchByInput
from dataRefresh import updateSearchData

#variables
cve_URL='https://cve.mitre.org/data/downloads/allitems.csv'
cve_DirName = './CVE_Downloads/'
cve_Filename = 'allitems.csv'
cve_FullPath = cve_DirName + cve_Filename
cve_FileType = '.csv'
lines2Remove = [",,,,,"]

# Remove outdated search data and update
if os.path.exists(cve_DirName):
    removeDirectory(cve_DirName)
    updateSearchData(cve_DirName, cve_URL, cve_Filename, cve_FullPath)
else:
    updateSearchData(cve_DirName, cve_URL, cve_Filename, cve_FullPath)

# Format file for import into list
fileFormat(cve_DirName, cve_Filename, lines2Remove)

# Search by keyword
searchByInput(cve_DirName, cve_Filename)