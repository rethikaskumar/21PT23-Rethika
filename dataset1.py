# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:16:01 2023

@author: DELL
"""

from PIL import Image
import json

file=open('input.json', 'r')
inputJson=json.load(file)
print(inputJson)

dieWidth=inputJson['die']['width']
dieHeight=inputJson['die']['height']

img=Image.open('wafer_image_1.png')
px=img.load()
print(px[10, 10])
