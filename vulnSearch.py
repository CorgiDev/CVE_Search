#imported modules
import os, shutil, requests, sys, csv
from fileEdit import appendNewRow, appendNewRowList, writeHeader, rowCountInt

def searchByInput(searchDataFile, resultFilePath):
    searchInput = ''
    searchInProgress = 'yes'
    while searchInProgress == 'yes':
        searchInput = input('Enter the CVE (CVE-####-####) you want to search for. You do not have to type the full label. For instance, you could search for "CVE-2014", "2014", or "CVE-2014-0178". Type "done" if finished. ')
        if searchInput.lower() == '':
            print("You didn't enter anything. Please try again.")
            continue
        elif searchInput.lower() == 'done':
            print("Exiting program.")
            break
        elif len(str(searchInput)) >= 1:
            # Write the results to the result file
            try:
                with open(searchDataFile) as searchData:
                    searchResults = []
                    csvReader = csv.reader(searchData, delimiter=',')
                    #next(csvReader)
                    rows = list(csvReader)
                    for row in rows[1:]:
                        for field in row[:1]:
                            fieldSearch = field.upper()
                            search = searchInput.upper()
                            if fieldSearch.find(search) >= 0:
                                searchResults.append(row)
                                appendNewRow(resultFilePath, row)
                resultCountInt = rowCountInt(resultFilePath)
                resultCount = str(resultCountInt-1)    
                if resultCountInt >= 2:
                    print("Search complete. " + resultCount + " results returned. See results in: " + resultFilePath)
                    searchInProgress = 'no'
                elif resultCountInt == 1:
                    print("There were no results for your search. Restart program and try again.")
                    searchInProgress = 'no'
            except UnicodeDecodeError as err:
                print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
    