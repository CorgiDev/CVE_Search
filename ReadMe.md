# Project Title
Brief description here. This program pulls down a list of Common Vulnerabilities and Exposures (CVEs) from https://cve.mitre.org/data/downloads/, and then imports it into a dictionary that can be searched.
![CVE site screenshot](/ReadMe-Files/00-screencapture.png)

## Pre-requisites
List of pre-requisites for running the program:
1. Have Python installed. Preferably 3.8.3+.
2. If running this within VS Code, you will want to: 
   1. Select the newest Python interpreter possible, and preferably a 64bit version.
   2. Install the Python extension authored by Microsoft.

## How to Launch Project
There are 2 methods to launch the program.
### If using VS Code
If you are using VS Code, the steps are a little simplified thanks to the *.vscode* folder. As long as you have set your python interpreter, you should be able to just press *F5* to start debug and it start the *main.py* file automatically.

### Running with Terminal
If you are using the terminal inside/outside VS Code, you will need to follow the commands below:
1. Navigate to the root folder of the project in a terminal, if not already there.
   1. You should see the *main.py* file if you use the `ls` command.
2. Run the following command: `py main.py install`
   1. If that doesn't work, you may need to try one of the following variants:
      1. `python main.py install`
      2. `C:\Python##\python.exe main.py install`
         1. The `##` needs to be replaced with the numbers matching the Python folder in your C drive. 
         2. For example, on my C drive, that folder is `Python38` so the path is `C:\Python38\python.exe`.
3. The application should start and run.
4. After running it with install once, subsequent runs should be able to be done without `install`.
   1.  In that case, the command would be: `py main.py`
       1.  Or, as before, if that does not work, you can try:
           1.  `python main.py`
           2.  `C:\Python##\python.exe main.py`

## Features Used:
The primary purpose of this section is to list optional requirements that were met when I used this for my Code Louisville project submission during the May 2020 Python course.
1. *Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program*
   1. A list is used by the csvReader in the *searchByInput* function in *vulnSearch.py* to read through the rows to find results.
   2. A list is used by the *rowCountInt* function in *extras.py* to return the number of rows, which is used by multiple other parts of the program.
2. *Read data from an external file, such as text, JSON, CSV, etc and use that data in your application*
   1. Downloads the CVE data file in CSV format.
   2. Edits it to get rid of some comment lines to avoid reading issues.
   3. Removes unnecessary rejected or reserved vuln labels.
      1. Reserved labels are ones that don't actually have a vuln attached to them yet.
      2. Rejected are ones that are not counted as vulns anymore. Could be in future, but this is part of why the file refreshes each time the program is run.
3. *Create and call at least 3 functions, at least one of which must return a value that is used*
   1. SOOOOO many functions everywhere.
   2. Multiple ones return values used to display: 
      1. Percentage search complete
      2. Number of records obtained from download after format
      3. Number of search results returned from search
      4. Updated file paths
4. *Analyze text and display information about it (ex: how many words in a paragraph)*
   1. I analyze the search data downloaded, once I have formatted it, to display how many search records are available to be searched.
   2. Once the results have been returned I display how many results were found, and let the user no if no results were found.