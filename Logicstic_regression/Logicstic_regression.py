import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd

# iris = datasets.load_iris()
# # print(iris)
# X = iris.data[:, :2]
# y = (iris.target != 0) * 1
# print(type(X), type(y))

my_data = pd.read_csv('./data.csv', names=["grade1", "grade2", "label"])  # read the data
print(my_data)
X = np.array(my_data.iloc[:, :2])
print(X)
y = np.array(my_data.iloc[:, 2:3]).flatten()
print(y)


class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    # adding column of 1 for matrix X
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    # PT dac trung
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # Cost function
    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, X, y):
        # Check data have intercept already or not yet
        if self.fit_intercept:
            X = self.__add_intercept(X)

        # weights initialization (khoi tao ma tran trong so)
        self.theta = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient

            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)

            if (self.verbose == True and i % 10000 == 0):
                print(f'loss: {loss} \t')

    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.theta))

    def predict(self, X):
        return self.predict_prob(X).round()


model = LogisticRegression(lr=0.1, num_iter=300000)

print(model.fit(X, y))
print(model.theta)

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
plt.legend()
x1_min, x1_max = X[:, 0].min(), X[:, 0].max(),
x2_min, x2_max = X[:, 1].min(), X[:, 1].max(),
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
probs = model.predict_prob(grid).reshape(xx1.shape)
print(xx1)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black')

# plt.show()
