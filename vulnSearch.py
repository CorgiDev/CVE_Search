#imported modules
import os, shutil, requests, sys, csv

# Search for item in list by CVE label
def searchByCVEName():
    print("Hello")


# Search for item based on phrase anywhere in the CVE description
def searchByAny(fileDir, fileName):
    fullFilePath = fileDir + fileName
    #input number you want to search
    searchTerm = input('Enter term you want to search for: ')
    #read csv, and split on "," the line
    csv_file = csv.reader(open(fullFilePath, "rb"), delimiter=",")
    #loop through csv list
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if searchTerm in row:
            print(row)

# ============================================================

""" searchTerm = input('What CVE Number do you want to search for? ')
if searchTerm.lower() != 'done':
    with open(fileName, newline='') as csvfile:
        vulnReader = csv.DictReader(csvfile, delimiter='')
        rows = list(vulnReader)
        for row in rows:
            print(row[searchTerm])
elif searchTerm.lower() == 'done'
break """

# Consider rewatching the string methods video in Python basics