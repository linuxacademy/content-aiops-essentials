import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import sys

sys.__stdout__ = sys.stdout

linear_regressor = LinearRegression()

#Read the actual metrics, the training data
dataset = pd.read_csv('promql.csv')

#Read new potential metrics to make projections
dataset2 = pd.read_csv('promql2.csv')

X = dataset[['replicas','memory']]
y = dataset['cpu']

X2 = dataset2[['replicas','memory']]
z2 = dataset2['replicas']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.9,random_state=0)

linear_regressor.fit(X_train,y_train)

pred_y = linear_regressor.predict(X2)

df = pd.DataFrame({'Projected Replicas':z2,'CPU Needed':pred_y})
print(df)
