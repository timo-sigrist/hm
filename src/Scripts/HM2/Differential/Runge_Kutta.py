import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def get_all_used_symbols(vector):
    """
    Takes an input vector, analyses all functions contained in it and returns all
    variables in a sorted array

    Parameters:

    vector: Function-vector, containing multiple functions

    Returns:

    symbols: all used variables in a sorted array

    """

    if hasattr(vector, '__iter__') is False:
        vector = sp.Matrix([vector])

    atoms = []
    for function in vector:
        variables = function.atoms(sp.Symbol)
        for variable in variables:
            if str(variable) not in atoms:
                atoms.append(str(variable))

    atoms.sort()
    symbols = []

    for atom in atoms:
        for function in vector:
            for variable in function.atoms(sp.Symbol):
                if str(variable) == atom and variable not in symbols:
                    symbols.append(variable)

    return symbols

def list_to_ndarray(list):
    ndarray = np.copy(list[0])

    for i, v in enumerate(list[1:]):
        ndarray = np.append(ndarray, v, axis=1)

    return ndarray

def init_runge_kutta(f):
    X = get_all_used_symbols(f)
    X.remove(x)
    expr = tuple([v] for i, v in enumerate(X)) if len(X) > 1 else X[0]

    f_func = sp.lambdify([x, expr], f, "numpy")

    return f_func


def runge_kutta(f, x0, y0, n, h):
    f_func = init_runge_kutta(f)

    x = [x0]
    y = [y0]

    k1 = []
    k2 = []
    k3 = []
    k4 = []

    for i in range(n):
        k1.append(f_func(x[i], y[i]))
        k2.append(f_func(x[i] + 1 / 2 * h, y[i] + 1 / 2 * h * k1[i]))
        k3.append(f_func(x[i] + 1 / 2 * h, y[i] + 1 / 2 * h * k2[i]))
        k4.append(f_func(x[i] + h, y[i] + h * k3[i]))
        x.append(x[i] + h)
        y.append(y[i] + h * 1 / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]))

    return x, y


if __name__ == "__main__":
    x, y = sp.symbols('x y')
    z1, z2, z3, z4 = sp.symbols('z1 z2 z3 z4')

    u = (300000.0 - 80000.0) / 190.0
    vrel = 2600.0
    ma = 300000.0
    g = 9.81
    f = sp.Matrix([z2, vrel * (u / (ma - u * x)) - g - (sp.exp(-z1 / 8000.0) / (ma - u * x)) * z2 ** 2])

    x0 = 0
    y0 = np.array([0.0, 0.0]).reshape(-1, 1)

    h = 0.1
    n = int(190 / h)

    x, y = runge_kutta(f, x0, y0, n, h)
    y = list_to_ndarray(y)

    def z3(t, z):
        u = (300000.0 - 80000.0) / 190.0
        vrel = 2600.0
        ma = 300000.0
        g = 9.81
        z1 = z[0]
        z2 = z[1]
        return vrel * (u / (ma - u * t)) - g - (np.exp(-z1 / 8000.0) / (ma - u * t)) * z2 ** 2

    plt.plot(x, y[0], label="h(t)")
    plt.title("h(t)")
    plt.grid()
    plt.figure()
    plt.plot(x, y[1], label="v(t)")
    plt.title("v(t)")
    plt.grid()
    plt.figure()
    plt.plot(x, [z3(x[i], y[:, i]) for i, v in enumerate(x)], label="a(t)")
    plt.title("a(t)")
    plt.grid()

    plt.show()


