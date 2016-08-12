import os
import cv2
import numpy as np

dir = "train"
dirGY = "trainGY"
listArray = os.listdir(dir)
listGYArray = os.listdir(dirGY)
for i in listArray:
    if i in listGYArray:
        continue
    imageArray = cv2.imread(dir + "/" + i, 0)

    colNum = imageArray.shape[1]
    addUnit = (40 - colNum)
    if addUnit % 2 == 0:
        unitArray = np.zeros([imageArray.shape[0], addUnit/2])
        cv2.imwrite("trainGY/" + i, np.concatenate((unitArray, imageArray, unitArray), axis=1))
    else:
        unitArray = np.zeros([imageArray.shape[0], addUnit / 2])
        unitArray1 = np.zeros([imageArray.shape[0], (addUnit / 2)+1])
        cv2.imwrite("trainGY/" + i, np.concatenate((unitArray, imageArray, unitArray1), axis=1))
