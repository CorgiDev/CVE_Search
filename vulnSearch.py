#imported modules
import os, shutil, requests, sys, csv

# Search for item in list by CVE label
def searchByCVEName():
    print("Hello")


# Search for item based on phrase anywhere in the CVE description
""" def searchByAny(fileDir, fileName):
    fullFilePath = fileDir + fileName
    #input number you want to search
    searchTerm = input('Enter term you want to search for: ')
    #read csv, and split on "," the line
    csv_file = csv.reader(open(fullFilePath, "rb"), delimiter=",")
    #loop through csv list
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if searchTerm in row:
            print(row) """

# ============================================================
def searchByAny(fileDir, fileName):
    fullFilePath = fileDir + fileName
    searchTerm = ''
    while searchTerm == '':
        searchTerm = input('What CVE Number do you want to search for? Type "done" if finished.')
        if searchTerm.lower() == 'done':
            break
        elif searchTerm.len() >= 1:
            with open(fullFilePath, newline='') as csvfile:
                vulnReader = csv.DictReader(csvfile, delimiter=',')
                rows = list(vulnReader)
                for row in rows:
                    print(row[searchTerm])

# Consider rewatching the string methods video in Python basics

""" username = input()

with open('Users.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') # good point by @paco
     for row in reader:
          for field in row:
              if field == username:
                  print "is in file" """