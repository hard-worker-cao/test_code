import numpy as np

data = np.array([(1, 9), (1.1, 10.5), (2, 18), (3, 28), (3.2, 30), (4, 37), (5, 48), (1.2, 10)])

X = data[:, 0]
y = data[:, 1]

# 截距项
X_b = np.c_[np.ones((len(X), 1)), X]
# 计算闭式解
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

X_new = np.array([[3.5], [4]])
X_new_b = np.c_[np.ones((2, 1)), X_new]  # 截距项
y_predict = X_new_b.dot(theta_best)
print(f"闭式解{y_predict}")

# 学习率
alpha = 0.01
# 迭代次数
iterations = 1000
m = len(X_b)
# 随机初始化参数
theta = np.random.randn(2, 1)
for iteration in range(iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y.reshape(-1, 1))
    theta = theta - alpha * gradients

# 预测
y_predict_ = X_new_b.dot(theta)
print(f"梯度下降{y_predict_.T}")

print(f"两者误差值为{abs(y_predict_ - y_predict.flatten())}")
