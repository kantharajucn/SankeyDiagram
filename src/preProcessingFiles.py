import csv
import os

#Listing all the files in that Directory data
allFiles = list(os.listdir(os.pardir+"/data"))

for aFile in allFiles:
    writecsvfile = open(os.pardir+"/output/"+aFile,"a")
    with open(os.pardir+"/data/"+aFile) as readcsvfile:
        reader = csv.DictReader(readcsvfile)
        for row in reader:
            curLine = str((row['id'], row['label'])).replace('(','').replace(')','')
            writecsvfile.write(str(curLine + "\n"))
