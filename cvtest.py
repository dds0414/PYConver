#  -*- coding: utf-8 -*-

import cv2
import Image
import numpy as np

name = "2"
# 灰度处理b
grayMat = cv2.imread('jpg/' + name + '.jpg', 0)
# 反转并去噪
binMat = 255 - grayMat
for indexRow, i in enumerate(binMat):
    for index, n in enumerate(i):
        if n < 25:
            binMat[indexRow][index] = 0
# print binMat.shape[1]
colArray = []
for col in range(binMat.shape[1]):
    res = 0
    for row in range(binMat.shape[0]):
        res += binMat[row][col]
    if res > 0:
        colArray.append(col)

print colArray[0], colArray[-1]

ceil = (colArray[-1] - colArray[0])/4
ceilArray = []
a = colArray[0]
for i in range(2):
    a += ceil
    ceilArray.append(a)
print ceilArray

# all
# cv2.imshow("image", binMat[:, colArray[0]:colArray[0]+30])
# cv2.imshow("image1", binMat[:, ceilArray[0]-2:ceilArray[0]-2+30])
# cv2.imshow("image2", binMat[:, ceilArray[1]-2:ceilArray[1]-2+30])
# cv2.imshow("image3", binMat[:, colArray[-1]-30:colArray[-1]])

cv2.imshow("image", binMat[:, colArray[0]:colArray[0]+30])
cv2.imshow("image1", binMat[:, ceilArray[0]-2:ceilArray[0]-2+30])
cv2.imshow("image2", binMat[:, ceilArray[1]-2:ceilArray[1]-2+30])
cv2.imshow("image3", binMat[:, colArray[-1]-30:colArray[-1]])


cv2.waitKey()
