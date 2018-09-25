# Gradient descent algorithm for linear regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# minimize the "sum of squared errors". This is how we calculate and correct our error
def compute_error_for_line_given_points(b, m, points):
    totalError = 0  # sum of square error formula
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
    # gradient descent
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - (m_current * x + b_current))
        m_gradient += -(2 / N) * x * (y - (m_current * x + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteartions):
    b = starting_b
    m = starting_m
    for i in range(num_iteartions):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]


def run():
    # Step 1: Collect the data
    points = np.genfromtxt('data.csv', delimiter=',')
    data = pd.read_csv('./data.csv')
    cols = data.shape[1]
    x = data.iloc[:, 0:cols - 1]
    y = data.iloc[:, cols - 1:cols]
    # Step 2: Define our Hyperparameters
    learning_rate = 0.0001  # how fast the data converge
    # y=mx+b (Slope formule)
    initial_b = 0  # initial y-intercept guess
    initial_m = 0  # initial slope guess
    num_iteartions = 1000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m,
                                                                              compute_error_for_line_given_points(
                                                                                  initial_b, initial_m, points)))

    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, 1000)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(1000, b, m,
                                                                      compute_error_for_line_given_points(b, m, points)))

    plt.figure(1)
    plt.scatter(x, y)
    equation = b + m * x
    plt.plot(x, equation, 'r', label='Prediction')
    plt.show()


# main function
if __name__ == "__main__":
    run()
