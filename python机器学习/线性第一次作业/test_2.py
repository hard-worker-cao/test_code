import numpy as np

data = np.array([
    [1, 2, 3, 20],
    [2, 3, 3, 25],
    [3, 2, 2, 21],
    [4, 2, 3, 28],
    [2, 3, 2, 22],
    [1, 2, 4, 23],
    [3, 3, 2, 25],
    [4, 4, 2, 29],
    [5, 5, 4, 43]
])

X = data[:, :3]
y = data[:, 3]

X_b = np.c_[np.ones((X.shape[0], 1)), X]

theta_normal = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

def predict(X, theta):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    return X_b.dot(theta)


x_test = np.array([[3, 3, 3]])
y_pred_normal = predict(x_test, theta_normal)


def compute_cost(X, y, theta):
    m = len(y)
    return (1 / (2 * m)) * np.sum((X.dot(theta) - y) ** 2)


def gradient_descent(X, y, theta, learning_rate, num_iterations):
    m = len(y)
    cost_history = np.zeros(num_iterations)

    for i in range(num_iterations):
        gradients = (1 / m) * X.T.dot(X.dot(theta) - y)
        theta = theta - learning_rate * gradients
        cost_history[i] = compute_cost(X, y, theta)

    return theta, cost_history


theta_initial = np.zeros(X_b.shape[1])
learning_rate = 0.01
num_iterations = 1000

theta_gd, cost_history = gradient_descent(X_b, y, theta_initial, learning_rate, num_iterations)

y_pred_gd = predict(x_test, theta_gd)

print(f"标准方程法{y_pred_normal}")
print(f"梯度下降法{y_pred_gd}")
