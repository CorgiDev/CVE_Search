#imported modules
import os, shutil

#imported functions
from functions import downloadFile
from functions import fileFormat
from functions import fileImport

#variables
cve_URL='https://cve.mitre.org/data/downloads/allitems.csv'
cve_DirName = './CVE_Downloads/'
cve_Filename = 'allitems.csv'
cve_FullPath = cve_DirName + cve_Filename
cve_FileType = '.csv'
lines2Remove = [",,,,,,"]

# Check if the directory exists. Remove/recreate if it does b4 downloading. 
# Create and start download if not.
if os.path.exists(cve_DirName):
    print("Old", cve_Filename, "exists.", "Removing outdated files.")
    shutil.rmtree(cve_DirName)
    print("Obtaining updated", cve_Filename)
    os.mkdir(cve_DirName)
    downloadFile(cve_URL, cve_Filename, cve_FullPath)
else:
    print("No existing", cve_Filename, ". Obtaining file now.")
    os.mkdir(cve_DirName)
    downloadFile(cve_URL, cve_Filename, cve_FullPath)

# fileFormat(cve_DirName, cve_Filename, lines2Remove)
# fileImport(cve_DirName, cve_Filename)