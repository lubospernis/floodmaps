#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:57:18 2019

@author: lubos
"""

import imageio
import numpy as np


img = imageio.imread('easy2.png')

Checked = []

def IsBlack(x, y, picture, bounds):
    condRed = 227
    RedLow = (condRed - condRed/bounds, condRed + condRed/bounds)
    
    condGreen = 85
    GreenLow = (condGreen - condGreen / bounds, condGreen + condGreen / 10)
    
    condBlue = 79
    BlueLow =(condBlue - condBlue / bounds, condBlue + condBlue / bounds)
    
    isinRed = picture[x][y][0] >= RedLow[0] and picture[x][y][0] <= RedLow[1]
    isinGreen = picture[x][y][1] >= GreenLow[0] and picture[x][y][1] <= GreenLow[1]
    isinBlue = picture[x][y][2] >= BlueLow[0] and picture[x][y][2] <= BlueLow[1]
    
    if isinRed and isinGreen and isinBlue:
        return True
    else: 
        return False

def CheckSurroundings(list):
    pass
    
#
#def WanderUntilBlack(x, y, picture):
#    Black = []
#    xFirst = x
#    yFirst = y
#    while IsBlack(xFirst, yFirst, picture):
#        xSecond = x
#        YSecond = y
#        while IsBlack(xSecond, YSecond, picture):
#            Black.append((xSecond, yFirst))
#            Checked.append((xSecond, yFirst))
#            xSecond += 1
#        yFirst += 1
#        
#        
#        
#    return Checked
#
#WanderUntilBlack(0, 0, img)        
#
#max(Checked)
#min(Checked)

def CoordDist(coord1, coord2):
    xDiff = coord1[0] - coord2[0]
    yDiff = coord1[1] - coord2[1]
    
    dist = (xDiff**2 + yDiff**2) **(0.5)
    return dist

CoordDist((0, 0), (3, 4))


def WalkThePicture(picture):
    x = None
    y = None
    lenX = len(picture)
    lenY = len(picture[1])
    CountBlackDots = 0
    Checked = []
    Black = []
    
    for y in range(lenY):
        for x in range(lenX):
            if (x, y) in Checked:
                continue  
            if IsBlack(x,y, picture, 15):
                CountBlackDots += 1
                Black.append((x, y))
            Checked.append((x, y))
    return Black
        
coords = WalkThePicture(img)



def GetDistancesMatrix(coords):
    distances = []
    for one in coords:
        for two in coords:
            distances.append(CoordDist(one, two)) 
    save = np.array(distances).reshape(len(coords), len(coords))
    return save  
     
distMat = GetDistancesMatrix(coords)
#
#Houses = {}


#from sklearn.cluster import MeanShift
#clustering = MeanShift(bandwidth = 10).fit(coords)
#clustering
#clustering.labels_
#clustering.predict(coords)
#
#mylist = list(set(clustering.labels_))
#len(mylist)

from sklearn.cluster import DBSCAN
db = DBSCAN(eps=3, metric = 'precomputed')
predictions = db.fit_predict(distMat)

len(list(set(predictions)))
