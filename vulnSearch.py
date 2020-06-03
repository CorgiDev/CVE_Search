#imported modules
import os, shutil, requests, sys, csv

# TO DO LIST (Will remove once done.)
# [x] 1. Ask user for search input
# [x] 2. If user enters 'done' then end program
# [ ] 3. If user enters nothing, tell them no input was received and prompt for input. Remind them that done will exit the app.
# [ ] 4. If user enters something: 
#    [x] a. Print the header row to the new result file.
#    [ ] b. Search for user input in the csv.
#       [ ] i. If search input found in current row, add row to the new result file.
#       [ ] ii. Else skip the row.
#
# ============================================================
def searchByInput(fileDir, fileName):
    searchDataFile = fileDir + fileName
    resultFile = 'results.csv'
    resultFilePath = fileDir + resultFile
    searchInput = ''
    while searchInput == '':
        searchInput = input('What CVE Number do you want to search for? Type "done" if finished. ')
        # Add a elif or if in here to catch empty inputs and ask them to give input again.
        if searchInput.lower() == 'done':
            break
        elif len(str(searchInput)) >= 1:
        # Copy needed lines to Results.csv file
            try:
                with open(searchDataFile) as searchData, open(resultFilePath, 'w', encoding='utf-8') as newResultFile:
                    # First write the header row to the result file
                    i = 0
                    for line in searchData:
                        while i == 0:
                            i += 1
                            newResultFile.write(line)
                            
                    # Then write the results to the result file
                    """ for line in searchData:
                        if not any(searchTerms in line for searchTerms in searchInput):
                            newResultFile.write(line) """
            except UnicodeDecodeError as err:
                print('Weird decode error, "', err, '" occurred. This is a stupid error and safe to ignore.')
    print("Search complete. See results in: " + resultFilePath)