#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:18:02 2019

@author: lubos
"""

class GetNumHouses:
    def __init__(self, imageDir):
        """
        Inits the recognition of houses
        """
        import imageio
        import numpy as np 
        
        self.img = imageio.imread(imageDir)
        
        
    def GetImg(self):
        return self.img
    def SetColour(self, R, G, B, tolerance):
        """
        Insert the RGB for the search and the tolerance
        in %
        """
        self.R = (R - R*tolerance, R, R + R*tolerance)
        self.G = (G - G*tolerance, G, G + G*tolerance)
        self.B = (B - B*tolerance, B, B + B*tolerance)
           
        
    def GetColours(self):
        """
        Returns a list of three tuples
        """
        list1 = [self.R, self.G, self.B]
        return list1
    
    def CheckColour(self, x, y):
        """
        Do not call on its own
        """
        isinRed = self.img[x][y][0] >= self.R[0] and self.img[x][y][0] <= self.R[2]
        isinGreen = self.img[x][y][1] >= self.G[0] and self.img[x][y][1] <= self.G[2]
        isinBlue = self.img[x][y][2] >= self.B[0] and self.img[x][y][2] <= self.B[2]
        
        
        if isinRed and isinGreen and isinBlue:
            return True
        else: 
            return False
    
    def WalkThePicture(self):
        """
        Depending on the size of the picture this can take long
        """
        
        x = None
        y = None
        lenX = len(self.img)
        lenY = len(self.img[1])
        CountBlackDots = 0
        Checked = []
        Black = []
    
        for y in range(lenY):
            for x in range(lenX):
                if (x, y) in Checked:
                    continue  
                if self.CheckColour(x,y):
                    CountBlackDots += 1
                    Black.append((x, y))
                Checked.append((x, y))
        self.coords =  Black
        
        return Black
    
    def GetCoords(self):
        return self.coords
    
    def CoordDist(self, coord1, coord2):
        xDiff = coord1[0] - coord2[0]
        yDiff = coord1[1] - coord2[1]
    
        dist = (xDiff**2 + yDiff**2) **(0.5)
        return dist
    
    def GetDistances(self):
        """ 
        Computes distances
        """
        import numpy as np
        distances = []
        for one in self.coords:
            for two in self.coords:
                distances.append(self.CoordDist(one, two)) 
        save = np.array(distances).reshape(len(self.coords), len(self.coords))
        self.distanceMatrix = save
        return save 
    
    def PerformClustering(self, epsVal = 3):
        """
        Performs Clustering
        """
        from sklearn.cluster import DBSCAN
        db = DBSCAN(eps=epsVal, metric = 'precomputed')
        predictions = db.fit_predict(self.distanceMatrix)
        self.ClusterPred = predictions
       
    def GetDistanceMat(self):
        return self.distanceMatrix
    
    def GetPredictions(self):
        
        return self.ClusterPred
    
    def GetNumHouses(self):
        """
        returns the number of Houses on the picture
        """
        number = len(list(set(self.ClusterPred)))
        return number
        

