# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:00:59 2018

@author: tarique
"""
# predict the salary of employe with 2 years of experience, test score =9
#and interview score = 6
#predict the salary of employe with 112 years of experience, test score =10
#and interview score = 10
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import linear_model
!pip install word2number
from word2number import w2n

df = pd.read_csv('C:\Tarique\ML\hiringdata.csv')
df

#convert Experience column from word to number

df.experience = df.experience.fillna("zero")
df
df[['experience']] = df.experience.apply(w2n.word_to_num)
df

#fill the  test_score NaN value with mean value
import math
mean_test_score = math.floor(df['test_score(out of 10)'].mean()) # make it integer value
mean_test_score
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(mean_test_score)
df
#Now create Linear Regression object
reg = linear_model.LinearRegression()
reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df['salary($)'])

reg.coef_
reg.intercept_

reg.predict([[2, 9, 6]])

reg.predict([[12, 10, 10]])