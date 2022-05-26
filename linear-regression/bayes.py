# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(10)
t = np.random.rand(10)

def phi(x):
    s = 0.1 # ガウス基底の幅
    return np.append(1, np.exp(-(x - np.arange(0, 1 + s,s)) ** 2 / (2 * s * s)))

PHI = np.array([phi(x) for x in X])
w = np.linalg.solve(np.dot(PHI.T, PHI), np.dot(PHI.T, t)) 

alpha = 0.1
beta = 9.0
Sigma_N = np.linalg.inv(alpha * np.identity(PHI.shape[1]) + beta * np.dot(PHI.T, PHI))
mu_N = beta * np.dot(Sigma_N, np.dot(PHI.T, t))

# 正規分布の確率密度関数
def normal_dist_pdf(x, mean, var):
    return np.exp(-(x-mean) ** 2 / (2 * var) / np.sqrt(2 * np.pi * var))

# 2次形式(x^T A x を計算)
def quad_from(A, x):
    return np.dot(x, np.dot(A, x))

xlist = np.arange(0, 1, 0.01)
# ylist = [np.dot(w, phi(x)) for x in xlist]
tlist = np.arange(-1.5, 1.5, 0.01)
z = np.array([normal_dist_pdf(tlist, np.dot(mu_N, phi(x)), 1 / beta + quad_from(Sigma_N, phi(x))) for x in xlist]).T

plt.contourf(xlist, tlist, z, 5, cmap=plt.cm.binary)
plt.plot(xlist, [np.dot(mu_N, phi(x)) for x in xlist], 'r')
plt.plot(X, t, 'go')
plt.show()