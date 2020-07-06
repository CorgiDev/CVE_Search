# imported modules
import csv

# Counts number of rows in a csv and returns it


def rowCountInt(filePath):
    file = open(filePath)
    reader = csv.reader(file)
    lines = len(list(reader))
    return lines

# Format a number to display as a percentage


def formatPercentage(int2Convert):
    newPercentage = "{:.0%}".format(int2Convert)
    return newPercentage
