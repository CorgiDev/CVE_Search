#import
import os, shutil, urllib.request

def filePrep():
    print("Hello")

#defined functions
def obtainFile(url, dir, fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print("Obtaining updated", fileName)
        urllib.request.urlretrieve(url, dir)
    else:
        print("Obtaining updated", fileName)
        urllib.request.urlretrieve(url, dir)