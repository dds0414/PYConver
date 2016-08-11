#  -*- coding: utf-8 -*-

import cv2
import Image
import numpy as np

import Image

name = "18"
im = Image.open('image/a/' + name + '.jpg')
im = im.convert('RGB')
im.save('jpg/' + name + '.jpg')

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

# 8.jpg
cv2.imshow("image", binMat[:, colArray[0]:colArray[0]+30])
cv2.imshow("image1", binMat[:, ceilArray[0]-2:ceilArray[0]-2+30])
cv2.imshow("image2", binMat[:, ceilArray[1]-2:ceilArray[1]-2+30])
cv2.imshow("image3", binMat[:, colArray[-1]-30:colArray[-1]])

#
# cv2.imshow("image", binMat[:, 31:58])
# cv2.imshow("image1", binMat[:, 56:81])
# cv2.imshow("image2", binMat[:, 78:112])
# cv2.imshow("image3", binMat[:, 112:140])

# cv2.imshow("image", binMat[:, 31:66])
# cv2.imshow("image1", binMat[:, 60:90])
# cv2.imshow("image2", binMat[:, 88:108])
# cv2.imshow("image3", binMat[:, 108:132])

# cv2.imshow("image", binMat[:, 31:61])
# cv2.imshow("image1", binMat[:, 54:83])
# cv2.imshow("image2", binMat[:, 79:108])
# cv2.imshow("image3", binMat[:, 101:132])

# cv2.imshow("image", binMat[:, 31:56])
# cv2.imshow("image1", binMat[:, 56:81])
# cv2.imshow("image2", binMat[:, 81:106])
# cv2.imshow("image3", binMat[:, 106:132])

# cv2.imshow("image", binMat[:, 31:66])
# cv2.imshow("image1", binMat[:, 51:86])
# cv2.imshow("image2", binMat[:, 76:111])
# cv2.imshow("image3", binMat[:, 96:132])
cv2.waitKey()
