# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:33:42 2018

@author: tarique
"""

#Sklearn linear regression model generates slope m and intercept b
#Gradient descent also generates slope and intercept by using Mean Square error
#it is an algorithm to find the best fitting linear regression line


# this code is to make linear regression using sklearn and gradient descent
#compare the values for m and b

#code for sklearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math

def predict_using_sklearn():
    df = pd.read_csv('C:\Tarique\ML\Youtube_codebasic\Gradient_Descent\Exercisedata.csv')
    # here Y=cs and X = math
    reg = LinearRegression()
    reg.fit(df[['math']],df.cs)
    return reg.coef_,reg.intercept_
    #this function return m and b
    
predict_using_sklearn() # calling this func to see m and b

#now finding m and b using Gradient descent
def gradient_descent(x,y):
    m_curr = 0
    b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.001
    cost_previous = 0
    
     for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print ("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost, i))

    return m_curr, b_curr
    
if __name__ == "__main__":
    df = pd.read_csv("test_scores.csv")
    x = np.array(df.math)
    y = np.array(df.cs)

    m, b = gradient_descent(x,y)
    print("Using gradient descent function: Coef {} Intercept {}".format(m, b))

    m_sklearn, b_sklearn = predict_using_sklean()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))
        
    
