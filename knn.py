from sklearn import neighbors
from sklearn import datasets
import numpy as np
import math
import cv2


# knn = neighbors.KNeighborsClassifier()
# iris = datasets.load_iris()
# knn.fit(iris.data, iris.target)
# prdictedLabel = knn.predict([[8.8, 3.8, 5.7, 4.9]])
# print prdictedLabel


def getdata():
    pass


def euclideanDisatance(instance1, instance2):
    distance = 0.0
    for i in range(len(instance1)):
        distance += pow((float(instance1[i]) - float(instance2[i])), 2)
    return 1-distance/len(instance1)


if __name__ == u"__main__":
    d1 = cv2.imread('trainGY/1.jpg', 0)
    d2 = cv2.imread('trainGY/2.jpg', 0)
    d3 = cv2.imread('trainGY/3.jpg', 0)
    d4 = cv2.imread('trainGY/4.jpg', 0)
    d5 = cv2.imread('trainGY/5.jpg', 0)
    d7 = cv2.imread('trainGY/7.jpg', 0)
    d8 = cv2.imread('trainGY/8.jpg', 0)
    dx = d1/float(d1.max() - d1.min())
    dx2 = d2/float(d2.max() - d2.min())
    dx3 = d3/float(d3.max() - d3.min())
    dx4 = d4/float(d4.max() - d4.min())
    dx5 = d5/float(d5.max() - d5.min())
    dx7 = d7/float(d7.max() - d7.min())
    dx8 = d8/float(d8.max() - d8.min())
    print euclideanDisatance(dx7.reshape((1, 2400))[0], dx8.reshape((1, 2400))[0])
    # print euclideanDisatance(dx.reshape((1, 2400))[0], dx3.reshape((1, 2400))[0])
    # print euclideanDisatance(dx.reshape((1, 2400))[0], dx4.reshape((1, 2400))[0])
    # print euclideanDisatance(dx.reshape((1, 2400))[0], dx5.reshape((1, 2400))[0])
    # print euclideanDisatance(dx2.reshape((1, 2400))[0], dx3.reshape((1, 2400))[0])
    # print euclideanDisatance(dx2.reshape((1, 2400))[0], dx5.reshape((1, 2400))[0])

    # euclideanDisatance()
