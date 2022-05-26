# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(10)
t = np.random.rand(10)

def phi(x):
    return [1, x, x**2, x**3, x**4, x**5, x**6, x**7]

PHI = np.array([phi(x) for x in X])

# np.linalg.solve(A, b) は A^{-1}b を返す
lamd = 0.01
w = np.linalg.solve(lamd * np.identity(8) + np.dot(PHI.T, PHI), np.dot(PHI.T, t)) 

def f(w, x):
    return np.dot(w, phi(x)) # 式(1)
    # return w[0] + w[1] * x + w[2] * (x**2) + w[3] * (x**3) # 式(3)

xlist = np.arange(0, 1, 0.001)
ylist = [f(w, x) for x in xlist]

plt.plot(xlist, ylist)
plt.plot(X, t, 'o')

plt.show()