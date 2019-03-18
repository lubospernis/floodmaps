#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:11:03 2019

@author: lubos
"""

import cv2
import numpy


img = cv2.imread("index.png", cv2.IMREAD_GRAYSCALE)
threshold = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)
#_, contours , _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("shapes", img)


print('this one is shift.')

#cv2.destroyAllWindows()
