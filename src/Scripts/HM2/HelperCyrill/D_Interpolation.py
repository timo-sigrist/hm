from A_UtilityFunction import *
import numpy as np
import matplotlib.pyplot as plt


def get_lagrange_interpolation_function(x, y):
    # =============================================
    # Start Lagrange-Interpolation
    # (Polynom-Interpolation)
    # =============================================

    n = x.size
    lagrange = 0
    lagrange_polynom = [1] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            lagrange_polynom[i] *= (x1 - x[j]) / (x[i] - x[j])

    for i in range(n):
        lagrange += y[i] * lagrange_polynom[i]

    lagrange_func = sp.lambdify(x1, lagrange, "numpy")

    return lagrange_func


def get_spline_function(x, y):
    # =============================================
    # Start natürliche kubische Splinefunktion
    # (Spline-Interpolation)
    # =============================================

    n = x.size - 1

    a = np.copy(y[0:n])
    h = x[1:n + 1] - x[0:n]
    c = np.zeros(n + 1)

    A = np.zeros((n - 1, n - 1))

    for i in range(n - 1):
        A[i, i] = 2 * (h[i] + h[i + 1])

    for i in range(0, n - 2):
        A[i, i + 1] = h[i]
        A[i + 1, i] = h[i]

    z = 3 * ((y[2:n + 1] - y[1:n]) / h[1:n] - (y[1:n] - y[0:n - 1]) / h[0:n - 1])
    c[1:n] = np.linalg.solve(A, z)

    b = (y[1:n + 1] - y[0:n]) / h - h / 3 * (c[1:n + 1] + 2 * c[0:n])
    d = (c[1:n + 1] - c[0:n]) / (3 * h)

    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("d: ", d)

    spline_cubic_polynom_func_list = [[x[i], x[i + 1], sp.lambdify(x1, a[i] + b[i] * x1 + c[i] * x1 ** 2 + d[i] * x1 ** 3, "numpy")] for i in range(n)]

    def spline_cubic_polynom_func(x):
        i = next((j for j, v in enumerate(spline_cubic_polynom_func_list) if x <= v[1]), len(spline_cubic_polynom_func_list) - 1)
        t = x - spline_cubic_polynom_func_list[i][0]

        return spline_cubic_polynom_func_list[i][2](t)

    return spline_cubic_polynom_func


if __name__ == "__main__":
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')

    x = np.array([0.6, 0.7, 0.8])
    y = np.array([0.8136, 0.9967, 1.1944])
    x_search = 0.66

    lagrange_func = get_lagrange_interpolation_function(x, y)
    y_search = lagrange_func(x_search)

    print(y_search)

    x = np.array([4, 6, 8, 10])
    y = np.array([6, 3, 9, 0])
    xx = np.arange(x[0], x[-1], 0.1)

    spline_func = get_spline_function(x, y)
    yy = [spline_func(v) for i, v in enumerate(xx)]

    plt.plot(x, y, 'o')
    plt.plot(xx, yy, '-')
    plt.legend(['Stützpunkte', 'Interpolationspunkte'])
    plt.show()
