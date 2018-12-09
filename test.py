# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:27:36 2018

@author: tarique
"""

#%matplotlib inline 
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

digits = load_digits() 

dir(digits)
digits.data[0]

plt.gray()
for i in range(5):
    plt.matshow(digits.images[i])
    
digits.target[0:5]

from sklearn.cross_validation import train_test_split
#from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(digits.data, digits.target, test_size = 0.2)
len(x_train)
len(x_test)