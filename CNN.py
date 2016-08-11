# -*- coding: utf-8 -*-
from __future__ import (absolute_import, unicode_literals, print_function)

from sknn.mlp import Classifier, Convolution, Layer
from sklearn import datasets
from sklearn.cross_validation import train_test_split
import numpy as np


digits = datasets.load_digits()
X = digits.images
Y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

Z = np.array([X[13]])


nn = Classifier(
    layers=[
        Convolution('Rectifier', channels=12, kernel_shape=(3, 3), border_mode='full'),
        Convolution('Rectifier', channels=8, kernel_shape=(3, 3), border_mode='valid'),
        Layer('Rectifier', units=64),
        Layer('Softmax')],
    learning_rate=0.002,
    valid_size=0.2,
    n_stable=10,
    verbose=True)

nn.fit(X_train, y_train)

# print('\nTRAIN SCORE', nn.score(X_train, y_train))
# print('TEST SCORE', nn.score(X_test, y_test))

y_pred = nn.predict(Z)
print(y_pred)
# import matplotlib.pyplot as pylab
#
# for index, (image, label) in enumerate(zip(digits.images[:6], digits.target[:6])):
#     pylab.subplot(2, 6, index + 1)
#     pylab.axis('off')
#     pylab.imshow(image, cmap=pylab.cm.gray_r, interpolation='nearest')
#     pylab.title('Training: %i' % label)
#
# for index, (image, prediction) in enumerate(zip(X_test[:6], y_pred[:6])):
#     pylab.subplot(2, 6, index + 7)
#     pylab.axis('off')
#     pylab.imshow(image.reshape((8,8)), cmap=pylab.cm.gray_r, interpolation='nearest')
#     pylab.title('Predicts: %i' % prediction)
#
# pylab.show()

