######################################################
#Name: cleanUp.py
#Version: 1.0
#Description: Cleaning up the temporary files

######################################################
import os

DataFiles = (list(os.listdir(os.pardir+"/data/")))
OutputFiles = (list(os.listdir(os.pardir+"/output/")))
for f1 in OutputFiles:
    os.remove(os.pardir+"/output/"+f1)
for f2 in DataFiles:
    os.remove(os.pardir+"/data/"+f2)
print "Removing all the temporary files is done"