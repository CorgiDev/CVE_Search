#imported modules
import os, shutil

#imported functions
from functions import downloadFile
from functions import filePrep
from functions import clearDirByFileType

#variables
cve_URL='https://cve.mitre.org/data/downloads/allitems.csv'
cve_DirName = './CVE_Downloads/'
cve_Filename = 'allitems.csv'
cve_FullPath = cve_DirName + cve_Filename
cve_FileType = '.csv'
lines2Remove = ",,,,,,"

if os.path.exists(cve_DirName):
    print("Removing outdated files.")
    shutil.rmtree(cve_DirName)
    # os.remove(cve_FullPath)
    print("Obtaining updated", cve_Filename)
    downloadFile(cve_URL, cve_Filename, cve_FullPath)
else:
    print("Obtaining updated", cve_Filename)
    downloadFile(cve_URL, cve_Filename, cve_FullPath)