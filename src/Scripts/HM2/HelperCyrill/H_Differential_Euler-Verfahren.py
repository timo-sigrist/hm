import matplotlib.pyplot as plt

from A_UtilityFunction import *
import numpy as np
import sympy as sp


def init_euler(f):
    X = get_all_used_symbols(f)
    X.remove(x)
    expr = tuple([v] for i, v in enumerate(X)) if len(X) > 1 else X[0]

    f_func = sp.lambdify([x, expr], f, "numpy")

    return f_func


def euler_method(f, x0, y0, n, h):
    # =============================================
    # Start Euler Verfahren
    # =============================================
    f_func = init_euler(f)

    x = [x0]
    y = [y0]
    for i in range(n):
        x_next = x[i] + h
        y_next = y[i] + h * f_func(x[i], y[i])

        x.append(x_next)
        y.append(y_next)
        print(x_next, y_next)

    return x, y


def mittelpunkt_method(f, x0, y0, n, h):
    # =============================================
    # Start Mittelpunkt Verfahren
    # =============================================
    f_func = init_euler(f)

    x = [x0]
    y = [y0]
    for i in range(n):
        x_half = x[i] + h / 2
        y_half = y[i] + h / 2 * f_func(x[i], y[i])

        x_next = x[i] + h
        y_next = y[i] + h * f_func(x_half, y_half)

        x.append(x_next)
        y.append(y_next)
        print(x_next, y_next)

    return x, y


def modified_euler_method(f, x0, y0, n, h):
    # =============================================
    # Start modifizierter Euler Verfahren
    # =============================================
    f_func = init_euler(f)

    x = [x0]
    y = [y0]
    for i in range(n):
        x_next = x[i] + h
        y_next_euler = y[i] + h * f_func(x[i], y[i])

        k1 = f_func(x[i], y[i])
        k2 = f_func(x_next, y_next_euler)
        y_next = y[i] + h * (k1 + k2) / 2

        x.append(x_next)
        y.append(y_next)

        print(x_next, y_next)

    return x, y


if __name__ == '__main__':
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')
    z1, z2, z3, z4 = sp.symbols('z1 z2 z3 z4')
    x, y = sp.symbols('x y')

    f = x**2 + 0.1 * y

    a = -1.5
    b = 1.5
    n = 5
    h = (b - a) / n

    x0 = a
    y0 = 0

    x, y = euler_method(f, x0, y0, n, h)

    x_new = np.arange(a, b, h/100.)
    def y_exact(t):
        return (-10. * t ** 2. - 200. * t - 2000. + 1722.5 * np.exp(0.05 * (2 * t + 3)))


    plt.plot(x, y, x_new, y_exact(x_new))
    plt.legend(['Euler (klassisch)', 'exakt'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid('major')

    plt.show()

    # f = sp.Matrix([z2, z3, z4, sp.sin(x) + 5 - 1.1 * z4 + 0.1 * z3 + 0.3 * z1])
    #
    # n = 5
    # h = 0.1
    #
    # x0 = 0
    # y0 = np.array([0, 2, 0, 0]).reshape(-1, 1)
    #
    # euler_method(f, x0, y0, n, h)

    # f = sp.Matrix([z2, z3, 10 * sp.exp(-x) - 5 * z3 - 8 * z2 - 6 * z1])
    #
    # n = 5
    # h = 0.5
    #
    # x0 = 0
    # y0 = np.array([2, 0, 0]).reshape(-1, 1)
    #
    # euler_method(f, x0, y0, n, h)