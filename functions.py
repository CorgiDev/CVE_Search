#import
import os, shutil, urllib.request

#defined functions
def filePrep():
    print("Hello")

def obtainFile(url, dir, fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print("Obtaining updated", fileName)
        urllib.request.urlretrieve(url, dir)
    else:
        print("Obtaining updated", fileName)
        urllib.request.urlretrieve(url, dir)