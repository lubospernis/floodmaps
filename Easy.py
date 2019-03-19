#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:51:21 2019

@author: lubos
"""

class Count:
    def __init__(self, listDirs):
        self.pic = listDirs
        self.colors = []
    def DefColors(self, Name, R, G, B):
        self.colors.append((Name, R, G, B))
        
    def Run(self):
        import imageio
        f = open('results.txt', 'w')
        f.write('Village,ColDef,Count \n')
        
        for item in self.pic:
            img = imageio.imread(item)
            Pocty = []
            for colors in self.colors:
                pocet = len(img[img == [colors[1], colors[2], colors[3]]]) / 3
                Pocty.append((colors[0], pocet))
            
            for times in Pocty:
                f.write(item + ','+ str(times[0]) + ','+ str(times[1]) + '\n')
        f.close()
        return 'finished...'
            
list1 = ['images/index.png', 'images/easy.png']  
                  
process1 = Count(list1)

process1.DefColors('Black', 0, 0, 0)

process1.DefColors('White', 255, 255, 255)

process1.Run()
