# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:16:01 2023

@author: DELL
"""

from PIL import Image
import json
import pandas as pd
from collections import Counter

pixelList=[]
lastrow=[]

file=open('input.json', 'r')
inputJson=json.load(file)
#print(inputJson)

dieWidth=inputJson['die']['width']
dieHeight=inputJson['die']['height']


careAreas=inputJson['care_areas']

for k in range(1, inputJson['die']['rows']*inputJson['die']['columns']+1):
    img=Image.open('wafer_image_'+str(k)+'.png')
    px=img.load()
    
    #print(px[0, 53])
    #print(0%30)
    
    #careAreaWidth=careAreas[0]['bottom_right']['x']-careAreas[0]['top_left']['x']
    #careAreaHeight=(dieHeight-careAreas[0]['top_left']['y']-1)-(dieHeight-careAreas[0]['bottom_right']['y']-1)
#print(dieHeight-careAreas[0]['bottom_right']['y'])
   
    for j in range(dieHeight-careAreas[0]['top_left']['y'], dieHeight-careAreas[0]['bottom_right']['y']):
         for i in range(careAreas[0]['top_left']['x'], careAreas[0]['bottom_right']['x']): 
            #print(i, j)
            if ((j)%30==0 and px[i, j]!=(255, 255, 255)):
                pixelList.append([k, i, dieHeight-j-1])
            elif ((j)%30!=0 and px[i, j]!=(128, 128, 128)):
                pixelList.append([k, i, dieHeight-j-1])
            if (dieHeight-j-1==0 and px[i, j]!=(128, 128, 128)):
                print(k, i, dieHeight-j-1, px[i, j])



pixelDf=pd.DataFrame(pixelList)
pixelDf.to_csv('pixel1.csv', index=False, header=False)

'''
#using counter
for i in range(careAreaWidth):
    for j in range(careAreaHeight):
        count=Counter([px[i]])
'''