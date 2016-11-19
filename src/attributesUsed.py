########################################################
#Name: attributesUsed.py
#Version 1.0
#Description: This file is responsible for generating the attributes
#which are used for each Cluster
########################################################
import csv
import os
import itertools
from sankey import files,shipment_0,shipment_1,shipment_2
from _collections import defaultdict

'''Initialization'''
myTransitions = defaultdict(list)
shipClusters = defaultdict(list)

def getTransitions(aFile,shipmentName):

    with open(os.pardir+"/data/"+aFile) as readcsvfile:
        reader = csv.DictReader(readcsvfile)
        values  = shipClusters.get(shipmentName)
        for eachCluster in values:
            print(eachCluster)
            myTransitions[str(eachCluster)].append(reader.fieldnames)

def writeTransitions(htmlfile):
    rownum = 0
    htmlfile.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
        <head>
            <h1 align = "center">Attributes used in each Transition</h1>
            <style>
            table, th, td {
                border: 1px solid black;
            }
            th {
                text-align: left;
            }
            table {
                border-spacing: 5px;
            }
            </style>
        </head>""")
    htmlfile.write('<body>')
    htmlfile.write('<table style="width:50%" align="center"  bgcolor="Azure"  color = "deeppink">')
    htmlfile.write('<caption>Attributes List</caption>')
    colnames = []
    for keys in myTransitions.keys():
        colnames.append(keys)
   
    '''Generate table contents'''
    for key in colnames:
        htmlfile.write('<tr>') 
        htmlfile.write('<th color="blue">' + key + '</th>')   
        for data in myTransitions[key]:
            for singleData in data:
                if singleData == 'id' or singleData == 'label':
                    continue
                htmlfile.write('<td>' + singleData + '</td>')
            htmlfile.write('</tr>')
        rownum += 1
    htmlfile.write('</table>')

'''Calling Functions'''
os.remove('../sankey/html/attribute.html')
htmlfile = open('../sankey/html/attribute.html',"w")
shipClusters['shipment_0'] = shipment_0
shipClusters['shipment_1'] = shipment_1
shipClusters['shipment_2'] = shipment_2
for aFile,name in itertools.izip(files,sorted(shipClusters.keys())):
    getTransitions(aFile,name)
writeTransitions(htmlfile)
htmlfile.close() 