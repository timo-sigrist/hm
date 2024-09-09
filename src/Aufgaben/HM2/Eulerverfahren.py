import numpy as np

def euler(f, a, b, n: int, y0):
    h = (b - a) / n
    n = int(n + 1)
    y = np.zeros(n)
    x = np.linspace(a, b, int(n))
    y[0] = y0
    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def mittelpunkt(f, a, b, n, y0):
    h = (b - a) / n
    n = int(n + 1)
    y = np.zeros(n)
    x = np.linspace(a, b, int(n))
    y[0] = y0
    for i in range(n - 1):
        xh = x[i] + h / 2
        yh = y[i] + h / 2 * f(x[i], y[i])
        y[i + 1] = y[i] + h * f(xh, yh)
    return x, y

def modEuler(f, a, b, n, y0):
    h = (b - a) / n
    n = int(n + 1)
    y = np.zeros(n)
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    yi_euler = np.zeros(n)
    x = np.linspace(a, b, int(n))
    y[0] = y0
    for i in range(n - 1):
        yi_euler[i] = y[i] + h * f(x[i], y[i])
        k1[i] = f(x[i], y[i])
        k2[i] = f(x[i + 1], yi_euler[i])
        y[i + 1] = y[i] + h * (k1[i] + k2[i]) / 2
    return x, y

