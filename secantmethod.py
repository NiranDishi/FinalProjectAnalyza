import numpy as np
from math import e, cos


# Finding roots using the secant method
def secant_method(x0, x1, tol):
    x2 = 0
    min_section = x0
    max_section = x1
    iter = 1
    condition = True
    x1s = []
    x0s = []
    fx0s = []

    while condition:
        if f(x0) == f(x1):
            print("Divide by zero error!")
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        if x2 > max_section or x2 < min_section:
            x2 = None
            break
        x0s.append(x0)
        x1s.append(x1)
        fx0s.append(f(x0))
        x0 = x1
        x1 = x2
        iter += 1

        condition = abs(f(x2)) > tol
    if x2 is not None:
        for x0 in range(len(x0s)):
            print(f"iteration = {x0 + 1} x0 = {x0s[x0]}, x1 = {x1s[x0]}, f(x0) = {fx0s[x0]}")

        print("**************************************************************************")
        print(f"Section [{min_section:.2f} ,{max_section:.2f}]: Found solution after {iter} iterations: {x2}")
        print("**************************************************************************")


def f(x):
    return ##################FUNCTION IS HERE


if __name__ == "__main__":
    epsilon = 1e-6
    min_range = 0
    max_range = 3
    step = 0.5
    secant_section_list = []

    for i in np.arange(min_range, max_range, step):
        i = round(i, 2)
        if f(i) * f(i + 0.1) <= 0:
            secant_section_list.append((i, i + step))

    # Finding roots by secant method:
    print("---------------------------------------------------------------------------------------------")
    print("Roots by secant method for f(x) = (x * e ** (-x ** 2 + 5 * x)) * (2 * x ** 2 - 3 * x - 6):")
    print("--------------------------------------------------------------------------------------------")

    # Sending 2 X0 and X1 guesses for possible ranges for finding roots
    if len(secant_section_list) == 0:
        print("No roots were found using a secant method")
    else:
        for section in secant_section_list:
            secant_method(section[0], section[1], epsilon)
