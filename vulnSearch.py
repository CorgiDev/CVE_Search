#imported modules
import os, shutil, requests, sys, csv
from fileEdit import appendNewRow, appendNewRowList, writeHeader

# TO DO LIST (Will remove once done.)
# [x] 1. Ask user for search input
# [x] 2. If user enters 'done' then end program
# [x] 3. If user enters nothing, tell them no input was received and prompt for input. Remind them that done will exit the app.
# [ ] 4. If user enters something: 
#    [x] a. Print the header row to the new result file.
#    [ ] b. Search for user input in the csv.
#       [ ] i. If search input found in current row, add row to the new result file after the header row.
#       [ ] ii. Else skip the row.
#
# ============================================================

def searchByInput(searchDataFile, resultFilePath):
    searchInput = ''
    searchInProgress = 'yes'
    while searchInProgress == 'yes':
        searchInput = input('Enter term you want to use for search. Type "done" if finished. ')
        if searchInput.lower() == '':
            print("You didn't enter anything. Please try again.")
            continue
        elif searchInput.lower() == 'done':
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
                        for field in row:
                            fieldSearch = field.upper()
                            search = searchInput.upper()
                            if fieldSearch.find(search) >= 0:
                                searchResults.append(row)
                                appendNewRow(resultFilePath, row)
                    searchInProgress = 'no'
            except UnicodeDecodeError as err:
                print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
    print("Search complete. See results in: " + resultFilePath)
    