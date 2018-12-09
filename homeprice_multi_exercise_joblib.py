# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:00:59 2018

@author: tarique
"""
# predict the price of the home with 3000sqft, 3 bedroom and 40 years old
#and 2500sqft, 4 bedroom and 5 years old
#
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import linear_model

df = pd.read_csv('C:\Tarique\ML\Youtube_codebasic\Linear_regression\homeprice_multi.csv')
df

#handle NaN value in bedroom column , Get the median of the bedrooms
import math
median_bedrooms = math.floor(df.bedrooms.median()) # make it integer value
median_bedrooms

#Fill the NaN value with Median value of bedrooms
df.bedrooms= df.bedrooms.fillna(median_bedrooms) # fillna is a function used to fill NaN value with median_bedroom

df

#Now create Linear Regression object
model = linear_model.LinearRegression()
model.fit(df[['area', 'bedrooms', 'age']], df.price)

model.coef_
model.intercept_

model.predict([[3000, 3, 40]])

model.predict([[2500, 4, 5]])


import pickle
with open('C:\Tarique\ML\Youtube_codebasic\Linear_regression\model_pickle', 'wb') as f: #this write the model in the model_pickle file
    pickle.dump(model, f)  # model_pickle is created as a binary file
    
with open('C:\Tarique\ML\Youtube_codebasic\Linear_regression\model_pickle', 'rb') as f: #this read the model file model_pickle
    mp = pickle.load(f) # mp is the memory object where the model is saved
    
mp.predict([[3000, 3, 40]])

from sklearn.externals import joblib
joblib.dump(model,'C:\Tarique\ML\Youtube_codebasic\Linear_regression\model_joblib' )
mj = joblib.load('C:\Tarique\ML\Youtube_codebasic\Linear_regression\model_joblib')
mj.predict([[3000, 3, 40]])
mj.coef_
mj.intercept_

