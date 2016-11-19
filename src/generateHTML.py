#########################################################
#Name: generateHTML.py
#Version: 1.0
#Description: This file is responsible for generating the HTML file to display the Sankey Diagram
#Also responsible for displaying the attributes used for each cluster dynamically
#########################################################
from sankey import *
import randomColor
from attributesUsed import myTransitions

'''Initialization'''
os .remove('../sankey/html/sankey.html')
sankeyfile = open('../sankey/html/sankey.html',"w")
stacks = []
colourDict = {}
stack_alloc = """ """
colours_alloc = """ """
i = 0
j = 0
'''Initialization : Ends'''

'''Storing all the cluster names in list: Starts'''
stacks.extend(shipment_0)
stacks.extend(shipment_1)
stacks.extend(shipment_2)
'''Storing all the cluster names in list: Ends'''


'''Getting number of colors required'''
file_count = len(shipment_0)
req_colors = file_count
colours = randomColor.colourGen(req_colors)

'''Writing to sankey.html file'''
sankeyfile.write(""" <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html lang='en' xml:lang='en' xmlns='http://www.w3.org/1999/xhtml'>
        <head>
            <meta content='text/html; charset=utf-8' http-equiv='Content-Type' />  
            <title>Cluster Visualization using sankey diagram</title>
            <script src="../js/raphael.js" type="text/javascript"></script>
            <script src="../js/jquery.js" type="text/javascript"></script>
            <script src="../js/jquery-ui.js" type="text/javascript"></script>
            <script src="../js/sankey.js" type="text/javascript"></script>
            <script src="../js/jquery-3.1.1.min.js" type="text/javascript"></script>
            <link type="text/css" href="../css/jquery-ui.css" rel="stylesheet" />
            <link rel="stylesheet" href="../css/style.css" />
            <link rel="stylesheet" href="../css/screendivide.css" />
            <script type="text/JavaScript">
                $(document).ready(function(){
                    $('.cluster').off().on('click',function(e){
                        $this = $(this);
                        var clusterName = $this.attr('data-clustername');
                        $('.cluster-details').hide();
                        $('#'+ clusterName).show();      
                    });
                });
            </script>
        </head>
        <body>
            <div class="container">
            <div class="toppane" align="center"><h1 style='text-align: center; margin-bottom: 0'>Sankey Diagram for Subspace Clustering</h1></div>
            <div class="leftpane">
            <script type='text/javascript'>
                $(document).ready(function() {
                    var sankey = new Sankey();
                    sankey.y_space = 30;
                    sankey.right_margin = 300;
                    sankey.left_margin = 50;
            """)

''' Stack allocation to each cluster'''
for lst in sorted(list([shipment_0,shipment_1,shipment_2])):
    stack_alloc =  stack_alloc + """sankey.stack(%d,["%s"]); \n""" %(i, '","'.join(str(f) for f in sorted(lst)))
    i+=1
sankeyfile.write(stack_alloc)

'''Setting colors to stacks'''
for stk in sorted(shipment_0):
    colours_alloc =  colours_alloc + """ "%s" : "%s",\n""" %(stk, colours[j])
    colourDict[stk] = colours[j]
    j+=1
colours_alloc = colours_alloc[:-2]
sankeyfile.write("""sankey.convert_flow_values_callback = function(flow) {
            return flow * 0.09; // Pixels per TWh
        };
        sankey.convert_flow_labels_callback = function(flow) {
            return Math.round(flow);
        };""")
sankeyfile.write("sankey.setColors({" + colours_alloc + "});\n")

'''Setting Raw Data to STacks'''
finalTran = dict(Counter(sorted(transitions.values())));
counter = 0
setData_0 = """["""

'''First transition'''
for key_1,val_1 in sorted(dict(Counter(myFirstToSecondDict.values())).items(),key=lambda s: s[0]):
    s01 = key_1[:2]
    s11 = key_1[2:]
    setData_0 = setData_0 + """["%s",%d,"%s"],""" %(s01,val_1,s11)
setData_0 = setData_0[:-1] + """]"""
sankeyfile.write('sankey.setData(' + setData_0 + '); \n' )
sankeyfile.write("sankey.draw();\n")
for cls in shipment_0:
    setData_1 = """["""
    colorAlloc_1 = """ """
    for stk in sorted(shipment_1):
        colorAlloc_1 =  colorAlloc_1 + """ "%s" : "%s",\n""" %(stk, colourDict[cls])
    for key,val in sorted(finalTran.items(), key=lambda s: s[0]):
        s1 = key[:2]
        s2 = key[2:4]
        s3 = key[4:]
        if s1 == cls:
            setData_1 = setData_1 + """["%s",%d,"%s"],""" %(s2,val,s3)
    colorAlloc_1 = colorAlloc_1[:-2]
    setData_1 = setData_1[:-1]
    sankeyfile.write("sankey.setColors({" + colorAlloc_1 + "}); \n")
    sankeyfile.write('sankey.setData(' + setData_1 + ']);\n' )
    sankeyfile.write("sankey.redraw();\n")
sankeyfile.write("""});
    </script>
    <div id='sankey' style="width:900px;height:1000px">
      &nbsp;
    </div>
    </div> \n""")
sankeyfile.write('<div class="middlepane ScrollStyle"> \n');
sankeyfile.write('<table align="center" bgcolor="Azure"> \n');
sankeyfile.write('<tr><th><h2>Clusters</h2></th></tr> \n')

'''Displaying the Attributes used for each cluster'''
for keyname in sorted(stacks):
    sankeyfile.write('<tr><td align="center"><form> <input type="button" class="cluster" data-clustername="'+keyname+'" value="'+keyname+'" name="'+keyname+'"></form></td></tr> \n' );
sankeyfile.write('</table> \n');
sankeyfile.write('</div> \n');
sankeyfile.write('<div class="rightpane ScrollStyle"> \n');

for key,value in sorted(myTransitions.items()):
    sankeyfile.write('<table style="display:none" class="cluster-details" align="center" bgcolor="Azure" id="'+key+'"> \n');
    sankeyfile.write('<tr><th><h2>Attributes</h2></th></tr> \n');
    for vals in value:
        for myval in vals:
            sankeyfile.write("<tr><td>"+myval+"</td></tr>");
    sankeyfile.write('</table> \n');
sankeyfile.write("""
            </div>
        </div>    
    </body>
</html>
""");

sankeyfile.close()
if os.path.exists(os.path.join(os.pardir+"/sankey/html", 'sankey.html')):
    print "Successfully generated the HTML file"
else:
    print "HTML file generation failed"

