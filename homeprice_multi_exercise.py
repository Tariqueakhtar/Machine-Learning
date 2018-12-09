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

df = pd.read_csv('C:\Tarique\ML\homeprice_multi.csv')
df

#handle NaN value in bedroom column , Get the median of the bedrooms
import math
median_bedrooms = math.floor(df.bedrooms.median()) # make it integer value
median_bedrooms

#Fill the NaN value with Median value of bedrooms
df.bedrooms= df.bedrooms.fillna(median_bedrooms) # fillna is a function used to fill NaN value with median_bedroom

df

#Now create Linear Regression object
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)

reg.coef_
reg.intercept_

reg.predict([[3000, 3, 40]])

reg.predict([[2500, 4, 5]])