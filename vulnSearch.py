#imported modules
import os, shutil, requests, sys, csv

# Search for item in list by CVE label
def searchByCVEName():
    print("Hello")


# Search for item based on phrase anywhere in the CVE description
def searchByAny():
    searchTerm = input('What CVE Number do you want to search for? ')
    if searchTerm.lower() != 'done':
        with open(fileName, newline='') as csvfile:
            vulnReader = csv.DictReader(csvfile, delimiter='')
            rows = list(vulnReader)
            for row in rows:
                print(row[searchTerm])
    elif searchTerm.lower() == 'done'
    break

# Consider rewatching the string methods video in Python basics