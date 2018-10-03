
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

dataset = pd.read_csv('./student_scores.csv')
# print(dataset)

diabetes_X_train = dataset.iloc[:, :-1].values

diabetes_y_train = dataset.iloc[:, 1].values

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

print(regr)
# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_train)

print(regr.predict)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_train, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_train, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_train, diabetes_y_train,  color='gray')
plt.plot(diabetes_X_train, diabetes_y_pred, color='r', linewidth=2)

plt.xticks(())
plt.yticks(())

plt.show()