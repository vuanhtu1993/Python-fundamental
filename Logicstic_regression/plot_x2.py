import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd


def drawFunction(X, theta):
    x1 = X.iloc[:, 0:1]
    print(x1)
    return [theta[0] + theta[1] * x1, 3, 4]


plt.figure(1)
theta = [-605.23048544, 4.76304661, 4.73375034]
test_data = pd.read_csv('./test_data.csv', names=["grade1"])
print(test_data.iloc[:, :1])
plt.plot(test_data.iloc[:, :1], drawFunction(test_data, theta), color='r', label="Prediction")\

plt.show()