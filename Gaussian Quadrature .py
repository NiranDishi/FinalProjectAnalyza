import numpy as np

def gaussQuadrature(f,a,b,n):
    half = float(b-a)/2.
    mid = (a+b)/2.
    [x,w] = np.polynomial.legendre.leggauss(n)
    result =  0.
    for i in range(n):
        result += w[i] * f(half*x[i] + mid)
    result *= half
    return result

def TRY(x):
    return np.exp(x**2)

for i in range(1,10):  
    print(gaussQuadrature(TRY,0,1,i))

