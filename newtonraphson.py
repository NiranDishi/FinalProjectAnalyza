from math import e, cos, sin
import numpy as np


def f(x):
    return #########################FUNCTION IS HERE


def df(x):
    return #####################NIGZERET IS HERE


# Finding roots using the Newton Raphson method
def newton_raphson(x0, x1, eps):
    min_section = x0
    max_section = x1
    xn = x0
    iter = 1
    xn_list = []
    fnx_list = []
    dfxn_list = []

    while True:
        fxn = f(xn)
        Dfxn = df(xn)
        if (xn < min_section or xn > max_section) and xn < 0:
            xn = x1
        if xn < min_range or xn > max_range:
            break
        if Dfxn == 0:
            print("Zero derivative. No solution found.")
            break
        if abs(fxn) < eps:
            for i in range(len(xn_list)):
                print(f"iteration = {i + 1} xn = {xn_list[i]}, f(xn) = {fnx_list[i]}, f'(xn) = {dfxn_list[i]}")
            print("*" * 50)
            print(f"Section [{min_section:.1f} ,{max_section:.1f}]: Found solution after {iter} iterations: {xn}")
            print("*" * 50)
            break

        xn_list.append(xn)
        fnx_list.append(f(xn))
        dfxn_list.append(df(xn))
        xn = xn - fxn / Dfxn
        iter += 1


if __name__ == "__main__":
    epsilon = 1e-6
    step = 0.5
    min_range = 0
    max_range = 3
    newton_section_list = []

    # Check if there is a root in a certain value range (in increments of 0.1)
    for i in np.arange(min_range, max_range, step):
        i = round(i, 2)
        if f(i) * f(i + 0.1) <= 0:
            newton_section_list.append((i, i + step))

    # Finding roots by Newton Raphson method:
    print("-" * 70)
    print("Roots by Newton Raphson method:")
    print("-" * 70)

    # Sending X0 for which a root approximation is found
    if len(newton_section_list) == 0:
        print("No roots were found using a Newton Raphson method")
    else:
        for section in newton_section_list:
            newton_raphson(section[0], section[1], epsilon)
