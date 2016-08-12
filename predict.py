#  -*- coding: utf-8 -*-
import pickle
import os
import cv2
import numpy as np


testPic = "test/4236.jpg"
grayMat = cv2.imread(testPic, 0)
# 反转并去噪
binMat = 255 - grayMat
for indexRow, i in enumerate(binMat):
    for index, n in enumerate(i):
        if n < 25:
            binMat[indexRow][index] = 0
colArray = []
for col in range(binMat.shape[1]):
    res = 0
    for row in range(binMat.shape[0]):
        res += binMat[row][col]
    if res > 0:
        colArray.append(col)
ceil = (colArray[-1] - colArray[0])/4
ceilArray = []
a = colArray[0]
for i in range(2):
    a += ceil
    ceilArray.append(a)
testArray = []
testArray.append(binMat[:, colArray[0]:colArray[0]+30])
testArray.append(binMat[:, ceilArray[0]-2:ceilArray[0]-2+30])
testArray.append(binMat[:, ceilArray[1]-2:ceilArray[1]-2+30])
testArray.append(binMat[:, colArray[-1]-30:colArray[-1]])




predictArr = []
unitArray = np.zeros([60, 5])
z = 0
nn = pickle.load(open('nn1.pkl', 'rb'))
resultList = pickle.load(open('result.pkl', 'rb'))
for i in testArray:
    a = np.concatenate((unitArray, i, unitArray), axis=1)
    b = a.reshape((1, 2400))[0]
    # predictArr.append(b)
    # print r
    print resultList[np.argmax(nn.predict(np.array(b)))]
    # cv2.imshow("image"+str(z), np.concatenate((unitArray, i, unitArray), axis=1))
    z += 1
# print np.array(predictArr)
# cv2.imshow("image", binMat[:, colArray[0]:colArray[0]+30])
# cv2.imshow("image1", binMat[:, ceilArray[0]-2:ceilArray[0]-2+30])
# cv2.imshow("image2", binMat[:, ceilArray[1]-2:ceilArray[1]-2+30])
# cv2.imshow("image3", binMat[:, colArray[-1]-30:colArray[-1]])
# cv2.waitKey()



