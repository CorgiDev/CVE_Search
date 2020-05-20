#import
import os, shutil, requests

#defined functions
def filePrep():
    print("Hello")

def obtainFile(url, fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print("Obtaining updated", fileName)
        downloadFile(url, fileName)
    else:
        print("Obtaining updated", fileName)
        downloadFile(url, fileName)

def downloadFile(url, fileName):
    r = requests.get(url)
    with open(fileName, 'wb') as f:
        f.write(r.content)
    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)