# imported modules
import os
import shutil
import requests
import sys
import csv
from fileEdit import appendNewRow, appendNewRowList, writeHeader
from extras import rowCountInt, formatPercentage


def searchByInput(searchDataFile, resultFilePath):
    searchInput = ''
    searchInProgress = 'yes'
    while searchInProgress == 'yes':
        searchInput = input(
            'Enter the CVE (CVE-####-####) you want to search for. You do not have to type the full label, but doing so will ensure a more accurate search. Type "done" if finished. ')
        if searchInput.lower() == '':
            print("You didn't enter anything. Please try again.")
            continue
        elif searchInput.lower() in ['done', 'quit']:
            print("Exiting program.")
            break
        elif len(str(searchInput)) >= 1:
            # Write the results to the result file
            totalSearchRecordsInt = ((rowCountInt(searchDataFile))-1)
            rowsRead = 1
            percentageSearched = 0
            oldPercentage = "0%"
            percentageSearchedStr = "0%"
            try:
                with open(searchDataFile) as searchData:
                    searchResults = []
                    csvReader = csv.reader(searchData, delimiter=',')
                    rows = list(csvReader)
                    for row in rows[1:]:
                        for field in row[:1]:
                            fieldSearch = field.upper()
                            search = searchInput.upper()
                            if fieldSearch.find(search) >= 0:
                                searchResults.append(row)
                                appendNewRow(resultFilePath, row)
                        percentageSearched = (rowsRead/totalSearchRecordsInt)
                        percentageSearchedStr = formatPercentage(
                            percentageSearched)
                        if oldPercentage != percentageSearchedStr:
                            print("Search " + percentageSearchedStr + " complete")
                            oldPercentage = percentageSearchedStr
                            rowsRead += 1
                        else:
                            rowsRead += 1
                            continue
                resultCountInt = rowCountInt(resultFilePath)
                resultCount = str(resultCountInt-1)
                if resultCountInt >= 2:
                    print("Search complete. " + resultCount +
                          " results returned. See results in: " + resultFilePath)
                    searchInProgress = 'no'
                elif resultCountInt == 1:
                    print(
                        "There were no results for your search. Restart program and try again.")
                    searchInProgress = 'no'
            except UnicodeDecodeError as err:
                print('Weird decode error, "', err,
                      '" occurred. This is a stupid error and safe to ignore.')
