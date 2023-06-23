# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:16:01 2023

@author: DELL
"""

from PIL import Image
import json
import pandas as pd

pixelList=[]
lastrow=[]

file=open('input.json', 'r')
inputJson=json.load(file)
#print(inputJson)

dieWidth=inputJson['die']['width']
dieHeight=inputJson['die']['height']


careAreas=inputJson['care_areas']

img=Image.open('wafer_image_1.png')
px=img.load()

print(px[0, 53])
print(0%30)


for i in range(careAreas[0]['bottom_right']['x']-careAreas[0]['top_left']['x']):
    for j in range(careAreas[0]['top_left']['y']-careAreas[0]['bottom_right']['y']):
        if (j%30==0 and px[i, j]!=(255, 255, 255)):
            pixelList.append([i, dieHeight-j-1])
        elif (j%30!=0 and px[i, j]!=(128, 128, 128)):
            pixelList.append([i, dieHeight-j-1])
        if (j==599 and px[i, j]!=(128, 128, 128)):
            print(i, j, px[i, j])

'''
pixelDf=pd.DataFrame(pixelList)
pixelDf.to_csv('pixel1.csv', index=False, header=False)
'''