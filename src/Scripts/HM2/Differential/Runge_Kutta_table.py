import numpy as np
import matplotlib.pyplot as plt

c = 0
a = 0
b = 0

# Butcher Teableau for Runge-Kutta
coefficients = [
    [c],
    [c, a],
    [c, a, a],
    [c, a, a, a],
    [0, b, b, b, b]
]

def runga_kutta(f, a, b, n, y0):
    h = (b - a) / n
    x = a
    y = y0
    xs = [x]
    ys = [y]
    for _ in range(0, n):
        k1 = f(x + h * coefficients[0][0], y)
        k2 = f(x + h * coefficients[1][0], y + h * coefficients[1][1] * k1)
        k3 = f(x + h * coefficients[2][0], y + h * (coefficients[2][1] * k1 + coefficients[2][2] * k2))
        k4 = f(x + h * coefficients[3][0], y + h * (coefficients[3][1] * k1 + coefficients[3][2] * k2 + coefficients[3][3] * k3))
        k = h * (coefficients[4][1] * k1 + coefficients[4][2] * k2 + coefficients[4][3] * k3 + coefficients[4][4] *k4)
        x += h
        y += h * k
        xs.append(x)
        ys.append(y)
    return xs, ys

def f(t, y): return 1 - y/t

def f_exact(t): return t/2 + 9/(2*t)

a = 1
b = 6
h = 0.01
n = int((b-a)/h)
print(n)
y0 = 5
xs, ys = runga_kutta(f, a, b, n, y0)
plt.plot(xs, ys, label="runga kutta")
plt.plot(xs, f_exact(np.array(xs)), label="exact")
plt.legend()
plt.show()