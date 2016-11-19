################################################################
#sankey.py
#Generating the Core logic to develop Sankey Diagram
#Version 1.0
#Date: September, 2016
################################################################
import csv
import os
import re
from collections import Counter

'''Parameter Initialization: Start'''
myFirstDict = {}
transitions = {}
mysecondDict = {}
mySecondToThirdDict = {}
myThirdDict = {}
myFirstToSecondDict = {}
noTransition = {}
files = []
'''Parameter Initialization: Ends'''

'''Listing all the files in a Directory: Start'''
allFiles = (list(os.listdir(os.pardir+"/output/")))
for each_file in allFiles:
    if re.match(r'^D[0-9]S[0-9][A-Z]*[0-9].csv',each_file):
        files.append(each_file)
'''Listing all the files in a Directory: Ends'''

'''Function: Reading CSV File - Starts'''
def readFiles(fileName,dictionary):
    reader = csv.reader(open(os.pardir+"/output/"+ fileName), delimiter=',', quotechar=None)
    try:
        count = 0
        while True:
            line = str(reader.next()).replace('"','').replace('"','').replace("[",'').replace("]",'')
            key,value =  line.split(',')
            dictionary[key] = value
            count+= 1
    except StopIteration:
        pass
'''Function: Reading CSV File - Ends'''
   
'''Function: Code to replace the string values with A1,A2,A3 etc - Starts'''
def replaceLabel(label,dictionary,myList):
    count = 1
    for values in myList:
        for key_val,val_dict in dictionary.items():
            if values == val_dict:
                dictionary[key_val] = label + str(count)
            
        count+=1
'''Function: Code to replace the string values with A1,A2,A3 etc - Ends'''
        
'''Function: Comparing two dictionaries - Starts'''
def compareDict(firstDict,secondDict,resultDict):
    for key,value in firstDict.items():
        if key in secondDict.keys():
            resultDict[key] = value + secondDict[key]
        else:
            noTransition[key] = value
'''Function: Comparing two dictionaries - Ends''' 
                   
'''Function to Get the dictionary which contains complete transitions for the data - Starts'''
def getFinalDict(dict_1,dict_2,result_dict):
    for key,value in dict_1.items():
        if key in dict_2.keys():
            result_dict[key] = value + dict_2[key]
'''Function to Get the dictionary which contains complete transitions for the data - Ends'''

'''Processing first Shipment'''
readFiles(files[0],myFirstDict)
mylist_1 = list(set(myFirstDict.values())) 
replaceLabel('A',myFirstDict,mylist_1)

'''Processing second Shipment'''
readFiles(files[1],mysecondDict)
mylist_2 = list(set(mysecondDict.values()))
replaceLabel('B',mysecondDict,mylist_2)

'''Processing third Shipment'''
readFiles(files[2],myThirdDict)
mylist_3 = list(set(myThirdDict.values()))
replaceLabel('C',myThirdDict,mylist_3)

'''Comparing the dictionaries '''
compareDict(myFirstDict,mysecondDict,myFirstToSecondDict)
compareDict(mysecondDict,myThirdDict,mySecondToThirdDict)

'''Getting Final Dictionary'''
getFinalDict(myFirstToSecondDict,myThirdDict,transitions)

'''Writing Dictionary into File'''
transitions = {k[1:-1]:v for k,v in transitions.items()}
with open('../output/transition.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in transitions.iteritems():
        writer.writerow(row)

shipment_0 = list(set(myFirstDict.values()))
shipment_1 =  list(set(mysecondDict.values()))
shipment_2 =  list(set(myThirdDict.values()))
#########################################################################################