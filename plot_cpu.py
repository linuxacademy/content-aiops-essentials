import sklearn
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.__stdout__ = sys.stdout

dataset = pd.read_csv('promql.csv')
print(dataset.head())

dataset.plot(x='replicas',y='cpu')
plt.title('Replicas vs CPU(%)')
plt.xlabel('Replicas')
plt.ylabel('CPU(%)')
plt.show()
