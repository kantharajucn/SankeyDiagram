################################################
#randomColor.py
#Generating the random RGB colors
#Version 1.0
###############################################
import random
'''Generating random colours'''
def colourGen(trans):
    myColours = []
    for i in range(0,trans): 
        r = lambda: random.randint(0,255)
        myColours.append('#%02X%02X%02X' % (r(),r(),r()))
    return myColours    
