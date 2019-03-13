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
print(dataset.head())
#print(dataset.describe)

#dataset.plot(x='replicas',y='cpu')
#plt.title('Replicas vs CPU(%)')
#plt.xlabel('Replicas')
#plt.ylabel('CPU(%)')
#plt.show()

X = dataset[['memory','cpu']]
y = dataset['replicas']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

linear_regressor.fit(X_train,y_train)

coeff = pd.DataFrame(linear_regressor.coef_, X.columns, columns=['Coefficient'])
print(coeff)

pred_y = linear_regressor.predict(X_test)

df = pd.DataFrame({'Actual':y_test,'Predicted':pred_y})
print(df)

