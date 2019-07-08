import numpy as np
import pandas as pd
class LinearRegressionGD:
    def __init__(self, eta = 0.001, n_iters = 20):
        self.eta = eta
        self.n_iters = n_iters
    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]
    def fit(self, X, y):
        self.w = np.zeros(1+X.shape[0]) # no of cols in X + 1
        self.cost = []
        for i in range(self.n_iters):
            output = self.net_input(X)
            errors = y - output
            self.w[1:] += self.eta * X.T.dot(errors)
            self.w[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost.append(cost)
        return self
    def predict(self, X):
        return self.net_input(X)

# class Reg:
#     def __init__(self, n_iters = 20, eta = 0.001):
#         self.eta = eta
#         self.n_iters = n_iters
#     def net_input(self, X):
#         return np.dot(X, self.w[1:]) + self.w[0]
#     def fit(self, X, y):
#         self.cost = []
#         self.w = np.zeros(1 + X.shape[1])
#         for i in range(self.n_iters):
#             output = self.net_input(X)
#             errors = y - output
#             self.w[1:] += self.eta * X.T.dot(errors)
#             self.w[0] += self.eta * errors.sum()
#             cost = (errors**2) / 2.0
#             self.cost.append(cost)
#         return self
#     def predict(self, X):
#         self.net_input(X)

dataset = np.matrix([[1,4,9,16], [1,2,3,4]])
df = pd.DataFrame(data = dataset)
X = df.iloc[0,:]
y = df.iloc[1,:]
print(X)
lr = LinearRegressionGD()
lr.fit(X, y)
res = lr.predict(X)
print(res)
