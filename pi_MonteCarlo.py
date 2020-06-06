'''Estimation of the value of Pi by Monte Carlo Method(Stone throwing).
    main_loop() Calculates the points which are inside and which are outside and
   estimates a value of pi for a particular Monte Carlo step.
   calculationLoop() calculates the average value, deviation and percentage errors in the value of pi
   for a certain number of repetition of the main_loop().
   plot_loop1() plots the stones.
   plt_loop2() plots the values fom calculationLoop().'''

### Sahil Islam ###
### 01/06/2020 ###


import math
import matplotlib.pyplot as plt
import numpy as np


def main_loop():
    radius = 1
    step = 100000
    y_coordinate_of_points_inside = np.zeros(step) + radius
    y_coordinate_of_points_outside = np.zeros(step) + radius
    x_coordinate_of_points = np.zeros(step) + radius

    number_of_points_inside = 0
    number_of_points_outside = 0

    for i in range(step):
        x = np.random.uniform(-radius, radius)
        y = np.random.uniform(-radius, radius)
        d = x ** 2 + y ** 2

        if d <= radius * radius:
            y_coordinate_of_points_inside[i] = y
            number_of_points_inside = number_of_points_inside + 1
        else:
            y_coordinate_of_points_outside[i] = y
            number_of_points_outside = number_of_points_outside + 1

        x_coordinate_of_points[i] = x

    total_points = number_of_points_outside + number_of_points_inside

    pi = number_of_points_inside * 4 / (total_points)

    return pi, x_coordinate_of_points, y_coordinate_of_points_inside, y_coordinate_of_points_outside, step


def calculationLoop(iteration):
    piValues = []
    piMath = []
    piDeviation = []
    x = []
    percentError = []

    itr = iteration

    for i in range(itr):
        pi, x_coordinate_of_points, y_coordinate_of_points_inside, y_coordinate_of_points_outside, step = main_loop()
        piValues.append(pi)
        piMath.append(math.pi)
        x.append(i)
        deviation = abs(pi - math.pi)
        error = deviation * 100 / math.pi
        piDeviation.append(deviation)
        percentError.append(error)

    sumPi = np.sum(piValues)
    piAvg = float(sumPi / itr)

    return x, piValues, piMath, piDeviation, piAvg, percentError, step


def plot_loop1():
    pi, x_coordinate_of_points, y_coordinate_of_points_inside, y_coordinate_of_points_outside, step = main_loop()

    main_loop()
    plt.scatter(x_coordinate_of_points, y_coordinate_of_points_inside, marker='.')
    plt.scatter(x_coordinate_of_points, y_coordinate_of_points_outside, marker='.')
    plt.title(
        "Estimation of value of Pi by Monte Carlo Method\n Fitting Points inside a circle" + "\n" + "No. of Steps:" + str(
            step))

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()


def plot_loop2(iteration):
    x, piValues, piMath, piDeviation, piAvg, percentError, step = calculationLoop(iteration)

    plt.subplot(2, 2, 1)
    plt.scatter(x, piValues, marker='.', label='Computed Values')
    plt.plot(x, piMath, color='red', label="Value from 'math.pi'")
    plt.xlabel("Iteration")
    plt.ylabel("Values of Pi")
    plt.legend()
    plt.title(" 'Math.pi' value and Computed Value")

    plt.subplot(2, 2, 3)
    plt.plot(x, percentError)
    plt.xlabel("Iteration")
    plt.ylabel("Percentage Error")
    plt.title("Percentage Error in the calculation of Pi")

    plt.subplot(2, 2, 4)
    plt.scatter(x, piDeviation, marker='.')
    plt.xlabel("Iteration")
    plt.ylabel("Deviation")

    plt.title("Absolute Deviation in the value o Pi")

    plt.suptitle("Estimation of value of Pi by Monte Carlo Method" + " \n Monte Carlo Step= " + str(step) + "\n "
                                                                                                            "Average Points: " + str(
        iteration) + "\n Average Value of pi: " + str(piAvg))

    plt.subplots_adjust(0.08, 0.07, 0.94, 0.80, 0.20, 0.40)
    plt.show()

plot_loop1()