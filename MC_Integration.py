"""This program calculates integration based on Monte Carlo Simulation"""
'''***(It still has some bugs to be fixed)***'''
### Sahil Islam ###
### 05/04/2020 ###

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.exp(-x * x)


a = 0
b = 1
step = 100000
interval = float(b - a) / step

xs = []
ys = []

pointsX = np.linspace(a, b, step)
pointsY = np.random.uniform(f(a), f(b), step)

pointsYin = []
pointsYout = []

pointsXin = []
pointsXout = []

countIn = 0
countOut = 0

for i in np.arange(a, b, interval):
    xs.append(i)
    ys.append(f(i))

for j in range(step):
    if pointsY[j] <= f(xs[j]):
        pointsYin.append(pointsY[j])
        xxin = float(a + j * (b - a) / step)
        pointsXin.append(xxin)
        countIn += 1
    else:
        pointsYout.append(pointsY[j])
        xxout = float(a + j * (b - a) / step)
        pointsXout.append(xxout)
        countOut += 1

area = float(countIn * (b - a) * max(ys) / step)

print(area)

plt.plot(xs, ys, color='k')
plt.scatter(pointsXin, pointsYin, marker='.', color='green')
plt.scatter(pointsXout, pointsYout, marker='.', color='red')
plt.show()
