import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#Aufgabe A
def euler(f, a, b, n: int, y0):
    h = (b - a) / n
    n = int(n + 1)
    y = np.zeros(n)
    x = np.linspace(a, b, int(n))
    y[0] = y0
    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def f(t, y):
    return -0.5**2-1*0.5


#Aufgabe B

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


if __name__ == '__main__':
    #Aufgabe a)
    a = 0
    b = 20
    n = 40 # für schrittweite 0.5
    #Euler
    x, y = euler(f, a, b, n, 0)
    print(x)
    print(y)

    #Aufgabe b)
    x, y = sp.symbols('x y')
    z1, z2, z3, z4 = sp.symbols('z1 z2 z3 z4')

    f = sp.Matrix([-0.5**2-1*0.5])

    x0 = 0
    y0 = np.array([0.0, 0.0]).reshape(-1, 1)

    h = 0.1
    n = int(190 / h)

    x, y = runge_kutta(f, x0, y0, n, h)
    y = list_to_ndarray(y)

    plt.plot(x, y)
    plt.show()
