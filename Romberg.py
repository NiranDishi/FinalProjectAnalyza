import numpy
from math import e


# Function to calculate f(x)
def f(x):
    return math.sin(x**4+5*x-6) / (2*math.e**(-2*x+5))


def romberg(a, b, n):
    r = numpy.array([[0] * (n + 1)] * (n + 1), float)
    h = b - a
    r[0, 0] = 0.5 * h * (f(a) + f(b))

    powerOf2 = 1
    for i in range(1, n + 1):

        # Compute the halved step-size and use this to sum the function at
        # all the new points (in between the points already computed)

        h = 0.5 * h

        sum = 0.0
        powerOf2 = 2 * powerOf2
        for k in range(1, powerOf2, 2):
            sum = sum + f(a + k * h)

        # Compute the composite trapezoid rule for the next level of
        # subdivision.  Use Richardson extrapolation to refine these values
        # into a more accurate form.

        r[i, 0] = 0.5 * r[i - 1, 0] + sum * h

        powerOf4 = 1
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            r[i, j] = r[i, j - 1] + (r[i, j - 1] - r[i - 1, j - 1]) / (powerOf4 - 1)

    return r


if __name__ == "__main__":
    lower_limit = 0.5  # Lower limit
    upper_limit = 1  # Upper limit
    n = 10  # Number of interval
    epsilon = 1e-6

    temp_return_val = romberg(lower_limit, upper_limit, n)
    temp_return_val = temp_return_val[-1][-1]

    # Check the amount of sections required to achieve desired accuracy
    while epsilon > 1e-6:
        n += 1
        return_val = romberg(lower_limit, upper_limit, n)
        return_val = return_val[-1][-1]
        epsilon = abs(temp_return_val - return_val)
        if epsilon >= 1e-6:
            temp_return_val = return_val
        else:
            n -= 1

    romberg_temp = romberg(lower_limit, upper_limit, n)

    for i in range(len(romberg_temp)):
        for j in range(len(romberg_temp)):
            if romberg_temp[i][j] != 0:
                print(romberg_temp[i][j], end=" ")
        print(" ")

    print("*************************************")
    print(f"Section [{lower_limit}, {upper_limit}] is divided into n = {int(n)} "
          f"sections in order to achieve the accuracy of {epsilon}")
    print(f"Answer = {temp_return_val}")
