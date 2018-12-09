# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:26:23 2018

@author: tarique
"""

import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0 #initialize slope and intercept as 0
    iterations = 1000 # define number of baby steps u want to take
    n= len(x) # lenght of data point i.e number of observations
    learning_rate = 0.08 # this value is trial and error, u need to keep changing to get perfect slope and intercept
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr # get the y_predicted for each iteration
        #then u need to calculate the m derivative and b derivative
        cost = (1/n)* sum([val**2 for val in (y - y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted)) # m derivative
        bd = -(2/n)*sum(y-y_predicted) # b derivative
        #now calculate  m and b using learning rate
        #m = m - learning rate*m derivative
        #b = b - learning rate * b derivative
        m_curr = m_curr - learning_rate* md
        b_curr = b_curr - learning_rate* bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost,i))
        
x = np.array([1,2,3,4,5])    
y = np.array([5,7,9,11,13])
gradient_descent(x,y)    
    
    