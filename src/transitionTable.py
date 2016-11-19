###################################################
#Name: transitionTable.py
#Description: This file is responsible for generating
#the table for patient transition from one shipment to other shipment
#Version: 1.0
###################################################
import csv
import os

'''Open the CSV file for reading'''
reader = csv.reader(open('../output/transition.csv'))

'''Create the HTML file for output'''
os.remove('../sankey/html/transition.html')
htmlfile = open('../sankey/html/transition.html',"w")

'''Initialize rownum variable'''
rownum = 0
htmlfile.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
      <head>
        <h1 align = "center">Transition of Objects over a period of time</h1>
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
htmlfile.write("<tr>")
htmlfile.write("""<th align = "center"  colspan = "2"><h1 align = "center" > Transition of Objects</h1></td>""")
htmlfile.write('</tr>')
htmlfile.write('<tr>')
htmlfile.write('<th color="blue">' + "ID" + '</th>')
htmlfile.write('<th color="blue">' + "Transition" + '</th>')
htmlfile.write('</tr>')

'''generate table contents'''
for row in reader: 
    colnum = 0   
    htmlfile.write('<tr>')    
    for column in row:
        htmlfile.write('<td>' + column + '</td>')
    htmlfile.write('</tr>')
    rownum += 1
    if row == 4:
        break

htmlfile.write('</table>')
htmlfile.close()
exit(0)
###############################