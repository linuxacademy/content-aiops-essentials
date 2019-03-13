import sklearn
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.__stdout__ = sys.stdout

dataset = pd.read_csv('promql.csv')
print(dataset.head())

dataset.plot(x='replicas',y='memory')
plt.title('Replicas vs Memory(%)')
plt.xlabel('Replicas')
plt.ylabel('Memory(%)')
plt.show()
