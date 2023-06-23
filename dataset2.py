# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:38:43 2023

@author: DELL
"""

from PIL import Image, ImageChops
import json
import pandas as pd
from collections import Counter
import numpy as np

pixelList=[]
lastrow=[]

file=open('input.json', 'r')
inputJson=json.load(file)
print(inputJson)
file.close()

dieHeight=inputJson['die']['height']
dieWidth=inputJson['die']['width']

#new=Image.new(mode="RGBA", size=(1200,1000))
#new.show()

'''
excludePixels=[]
for x in inputJson['exclusion_zones']:
    start_width=x['top_left']['x']
    end_width=x['bottom_right']['x']
    start_height=dieHeight-x['top_left']['y']
    end_height=dieHeight-x['bottom_right']['y']
    print(start_height, end_height, start_width, end_width)
    for j in range(start_height, end_height):
        for i in range(start_width, end_width):
            #print((i, j))
            excludePixels.append((i, j))

#print(excludePixels)
carePixels=[]
for x in inputJson['care_areas']:
    start_width=x['top_left']['x']
    end_width=x['bottom_right']['x']
    start_height=dieHeight-x['top_left']['y']
    end_height=dieHeight-x['bottom_right']['y']
    print(start_height, end_height, start_width, end_width)
    for j in range(start_height, end_height):
        for i in range(start_width, end_width):
            print((i, j))
            a=(i, j)
            if a not in excludePixels:
                carePixels.append(a)

print(carePixels)
img1=Image.open('wafer_image_1'+'.png')
px1=img1.load()
fx=new.load()
fx=px1
for x, y in carePixels:
    fx[x, y]=(0, 0, 0)
new.show()
    

start_width_exc=[x['top_left']['x'] for x in inputJson['exclusion_zones']]
end_width_exc=[x['bottom_right']['x'] for x in inputJson['exclusion_zones']]
start_height_exc=[dieHeight-x['top_left']['y'] for x in inputJson['exclusion_zones']]
end_height_exc=[dieHeight-x['bottom_right']['y'] for x in inputJson['exclusion_zones']]

start_width_care=[x['top_left']['x'] for x in inputJson['care_areas']]
end_width_care=[x['bottom_right']['x'] for x in inputJson['care_areas']]
start_height_care=[dieHeight-x['top_left']['y'] for x in inputJson['care_areas']]
end_height_care=[dieHeight-x['bottom_right']['y'] for x in inputJson['care_areas']]

print(end_height_care)


defectset=set()
totalset=set()
'''

mainlist=[]
'''
for s in range(1, 16):
    list1=[]
    img1=Image.open('wafer_image_'+str(s)+'.png')
    px1=img1.load()
    #fpx=new.load()
    t=(s)%15+1
    img2=Image.open('wafer_image_'+str(t)+'.png')
    px2=img2.load()
    diff=ImageChops.difference(img1, img2)
    diffpx=diff.load()
    for j in range(0, 1000):
         for i in range(0, 1200): 
            if diffpx[i, j]!=(0, 0, 0):
                list1.append([s, i, dieHeight-j-1])
    for k in range(s+1, s+16):
        list2=[]
        if (k%15+1)!=s and (k%15+1)!=s+1:
            print('wafer_image_'+str(k%15+1))
            img2=Image.open('wafer_image_'+str(k%15+1)+'.png')
            px2=img2.load()
            diff=ImageChops.difference(img1, img2)
            diffpx=diff.load()
            for j in range(0, 1000):
                 for i in range(0, 1200): 
                    if diffpx[i, j]!=(0, 0, 0):
                        list2.append([s, i, dieHeight-j-1])
            list1=[x for x in list1 if x in list2]
    mainlist.extend(list1)


df1=pd.DataFrame(mainlist)
df1.to_csv('check1.csv', index=False, header=False)

'''
'''
for k in range(2, 3):
    img2=Image.open('wafer_image_'+str(k)+'.png')
    px2=img2.load()
    diff=ImageChops.difference(img1, img2)
    diffpx=diff.load()
    for sj, ej in zip(start_height_care, end_height_care):
        #print("sj, ej: ", (sj, ej))
        for j in range(sj, ej):
            for sjx, ejx in zip(start_height_exc, end_height_exc):
                #print("sjx, ejx: ", (sjx, ejx))
                for si, ei in zip(start_width_care, end_height_care):
                    for six, eix in zip(start_width_exc, end_width_exc):    
                        for i in range(si, ei):
                            if i in range(six, eix) and j in range(sjx, ejx):
                                fpx[i, dieHeight-j-1]=(0, 0, 0)
                            else:
                                totalset.add((i, dieHeight-j-1))
                                if diffpx[i, dieHeight-j-1]!=(0, 0, 0):
                                    fpx[i, dieHeight-j-1]=(0, 0, 0)
                                    defectset.add((i, dieHeight-j-1))
                                else:
                                    fpx[i, dieHeight-j-1]=px1[i, dieHeight-j-1]
                                    
print(defectset)
new.show()

#new=Image.fromarray(array)
#new.show()

'''

for s in range(1, 16 ):
    list1=[]
    img1=Image.open('wafer_image_'+str(s)+'.png')
    px1=img1.load()
    #fpx=new.load()
    t=(s%15)+1
    img2=Image.open('wafer_image_'+str(t)+'.png')
    px2=img2.load()
    diff=ImageChops.difference(img1, img2)
    diffpx=diff.load()
    for j in range(0, 1000):
         for i in range(0, 1200): 
            if diffpx[i, j]!=(0, 0, 0):
                list1.append([s, i, dieHeight-j-1])
    t=(t%15)+1
    list2=[]
    img2=Image.open('wafer_image_'+str(t)+'.png')
    px2=img2.load()
    diff=ImageChops.difference(img1, img2)
    diffpx=diff.load()
    for j in range(0, 1000):
         for i in range(0, 1200): 
            if diffpx[i, j]!=(0, 0, 0):
                list2.append([s, i, dieHeight-j-1])
    l3=[]
    for x in list1:
        if x in list2:
            l3.append(x)
    mainlist.extend(l3)


df1=pd.DataFrame(mainlist)
df1.to_csv('check1.csv', index=False, header=False)
