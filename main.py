#imported modules

#imported functions
from functions import obtainFile
from functions import filePrep

#variables
cve_url='https://cve.mitre.org/data/downloads/allitems.csv'
dirName = '.'
fileName = 'allitems.csv'

obtainFile(cve_url, fileName)