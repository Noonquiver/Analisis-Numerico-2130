# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

p = 4

def f(x):
    return (x + 1)**(1/2)

print("Polinomio de Taylor: ")
print(approximate_taylor_polynomial(f, 1, p, 3/2))
print("")

for n in range(0, p + 1):
    error = abs(approximate_taylor_polynomial(f, 1, p, 3/2)[n])
    print(f"Error en P({n}): ")
    print(error)
    print("")

