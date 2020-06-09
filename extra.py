#imported modules
import os, shutil, requests, sys, csv
from fileEdit import appendNewRow, appendNewRowList, writeHeader

# TO DO LIST (Will remove once done.)
# [x] 1. Ask user for search input
# [x] 2. If user enters 'done' then end program
# [x] 3. If user enters nothing, tell them no input was received and prompt for input. Remind them that done will exit the app.
# [ ] 4. If user enters something: 
#    [ ] a. Search for user input in the csv.
#       [ ] i. If search input found in current row, add row to the new result file after the header row.
#       [ ] ii. Else skip the row.
#
# ============================================================

def gatherInput(fileDir, fileName, resultFilePath):
    searchDataFile = fileDir + fileName
    searchInput = ''
    while searchInput != 'done':
        searchInput = input('Enter term you want to use for search. Type "done" if finished. ')
        if searchInput.lower() == '':
            print("You didn't enter anything. Please try again.")
            continue
        elif searchInput.lower() == 'done':
            break
        elif len(str(searchInput)) >= 1:
            searchByInput(searchDataFile, resultFilePath, searchInput)
            searchInput = 'done'
    print("Search complete. See results in: " + resultFilePath)

def searchByInput(searchDataFile, resultFilePath, searchInput):
    # Copy needed lines to Results.csv file
    # IMPORTANT - I need to really make the search skip the header row so I don't end up accidentally writing it to the file again.
    search = searchInput.upper()
    i = 0
    while i == 0:
        try:
            with open(searchDataFile) as searchData:
                searchResults = []
                csvReader = csv.reader(searchData, delimiter=',')
                next(csvReader)
                for row in csvReader:
                    for field in row:
                        fieldSearch = field.upper()
                        if fieldSearch.find(search) >= 0:
                            searchResults.append(row)
                            appendNewRow(resultFilePath, row)
                searchDataFile.close()
                i += 1
        except UnicodeDecodeError:
            #print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
            pass
    print("Search complete. See results in: " + resultFilePath)
    