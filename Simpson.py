# Python code for simpson's 1 / 3 rule
from _ctypes_test import func
from math import e, cos
import numpy as np


# Function to calculate f(x)
def f(x):
    return math.sin(x**4+5*x-6) / (2*math.e**(-2*x+5))



# Function for approximate integral
def simpson(ll, ul, n):
    # Calculating the value of h
    h = (ul - ll) / n

    # List for storing value of x and f(x)
    x = list()
    fx = list()

    # Calcuting values of x and f(x)
    i = 0
    while i <= n:
        x.append(ll + i * h)
        fx.append(f(x[i]))
        i += 1

    # Calculating result
    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    res = res * (h / 3)
    return res


if __name__ == "__main__":
    lower_limit = -0.5  # Lower limit
    upper_limit = 0.5  # Upper limit
    n = 10  # Number of interval
    epsilon = 1e-6

    temp_return_val = simpson(lower_limit, upper_limit, n)

    # Check the amount of sections required to achieve desired accuracy
    while epsilon >= 1e-6:
        print(f"n = {n}, Answer = {temp_return_val}")
        n *= 2
        return_val = simpson(lower_limit, upper_limit, n)
        epsilon = abs(temp_return_val - return_val)
        if epsilon >= 1e-6:
            temp_return_val = return_val
        else:
            n /= 2

    print(
        f"Section [{lower_limit}, {upper_limit}] is divided into n = {int(n)} "
        f"equal sections in order to achieve the accuracy of 0.0001")
    print(f"Answer = {temp_return_val}")
