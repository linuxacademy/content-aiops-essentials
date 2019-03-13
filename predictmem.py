import sklearn
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.__stdout__ = sys.stdout

linear_regressor = LinearRegression()

dataset = pd.read_csv('promql.csv')
dataset2 = pd.read_csv('promql2.csv')
#print(dataset.head())
#print(dataset.describe)

X = dataset[['replicas','cpu']]
y = dataset['memory']

X2 = dataset2[['replicas','cpu']]
y2 = dataset2['memory']
z2 = dataset2['replicas']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.9,random_state=0)

linear_regressor.fit(X_train,y_train)

pred_y = linear_regressor.predict(X2)

df = pd.DataFrame({'Projected Replicas':z2,'Mem Increase (%)':pred_y})
print(df)

