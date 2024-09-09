from A_UtilityFunction import *
import numpy as np
import sympy as sp

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')

f = 1 / x1
a = 2
b = 4
m = 4

# =============================================
# Start Romberg-Extrapolation
# =============================================

f_func = sp.lambdify(x1, f)

romberg_matrix = np.zeros((m, m))
romberg_err_matrix = np.zeros((m, m))

x = np.linspace(a, b)

for j in range(0, m, 1):
    h = (b - a) / 2 ** j
    n = 2 ** j
    res = (f_func(a) + f_func(b)) / 2
    for i in range(1, n):
        xi = a + i * h
        res += f_func(xi)

    res *= h

    romberg_matrix[j, 0] = res
    romberg_err_matrix[j, 0] = abs(res - np.trapz(f_func(x), x))

for k in range(1, m):
    for j in range(m-k-1, -1, -1):
        romberg_matrix[j, k] = (4 ** k * romberg_matrix[j+1, k-1] - romberg_matrix[j, k-1]) / (4 ** k - 1)
        romberg_err_matrix[j, k] = abs(romberg_matrix[j, k] - np.trapz(f_func(x), x))

print(romberg_matrix)
print(romberg_matrix[0, m-1])
