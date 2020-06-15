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
1. Navigate to the root folder of the project in a terminal if not already there.
   1. You should see the main.py file if you use the `ls` command.
2. Run the following command: `py main.py install`
   1. If that doesn't work you may need to try one of the following variants:
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
1. *Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program*
2. *Read data from an external file, such as text, JSON, CSV, etc and use that data in your application*
3. *Create and call at least 3 functions, at least one of which must return a value that is used*
   1. 
4. Checks if the *CVE_Downloads* folder it needs exists.
   1. If not it creates it before downloading the file.
   2. If it does, it removes it to get rid of outdated files and recreates it before downloading.


## Additional Notes

Additional notes on the project.

## Resources

- [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

=========================================

Everything below here will be deleted 
once the project is complete.

=========================================

## Possible project ideas
1. CVE page
   1. Downloads csv file from external source.
   2. Reads the file, edits it to prepare to pull it in.
   3. Converts the edited contents into a dictionary/list.
   4. Add 3 functions.
      1. One that edits the file.
2. b
3. c

## Project Requirements according to syllabus
I'll delete this section once I get my project completed.

### **Requirements:**
Choose a **minimum of 3** of the below features and incorporate into your site
- [] Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
- [] Create a class, then create at least one object of that class and populate it with data
- [x] Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
- [] Implement a log that records errors, invalid inputs, or other important events and writes them to a text file
- [x] Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
- [x] Create and call at least 3 functions, at least one of which must return a value that is used
- [] Implement a regular expression (regex) to ensure a field either a phone number or an email address is always stored and displayed in the same format
- [] Connect to an external/3rd party API and read data into your app
- [] Create 3 or more unit tests for your application
- [] Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams)
- [] Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)
- [] Analyze text and display information about it (ex: how many words in a paragraph)
  - How I used this:
    - I analyze the file format and 
- [] Visualize data in a graph, chart, or other visual representation of data
- [] Other features can be added to this list - just ask if your project needs something specific and as long as it’s a good demonstration of your programming skills, it almost certainly will count!  Basically, we just want to see you do something interesting and challenging!

### Additional Requirements
**ALL** of the below requirements must be met.
- [x] Your code have comments that document major sections of your code to make it easier to read
  - You don’t need to go crazy on this - a few code comments are perfectly fine
- [x] It must include a README file located at the top level directory of your project that includes:
  - A description of your project
  - What features you chose to included (so we know what to look for)
  - Any special instructions we might need to run your project