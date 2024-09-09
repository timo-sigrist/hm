import numpy as np
import sympy as sp
from scipy import optimize


def recheck_method(f, a, b):
    return f((a + b) / 2) * (b - a)


def trapez_method(f, a, b):
    return (f(a) + f(b)) / 2 * (b - a)


def simpson_method(f, a, b):
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) / 2) + f(b))


def sum_rechteck_method(f, a, b, n: int):
    h = (b - a) / n  # Abstand zwischen zwei Stützstellen

    support = np.linspace(a, b - h, n)
    sum_pommes = np.array([f(x + (h / 2)) for x in support]).sum()

    return h * sum_pommes


def sum_trapez_method(f, a, b, n: int):
    h = (b - a) / n  # Abstand zwischen zwei Stützstellen

    support = np.linspace(a + h, b, n)[:-1]
    sum_trapez = np.array([f(x) for x in support]).sum()

    return h * (sum_trapez + ((f(a) + f(b)) / 2))


def simplified_sum_simpson_method(f, a, b, n: int):
    return (1 / 3) * (sum_trapez_method(f, a, b, n) + 2 * sum_rechteck_method(f, a, b, n))


def sum_simpson_method(f, a, b, n: int):
    """
    f: Funktion, welche integriert werden soll
    a: Unterer Grenzwert
    b: Oberer Grenzwert
    n: Anzahl Stützstellen
    """
    h = (b - a) / n  # Abstand zwischen zwei Stützstellen
    support = np.arange(a, b + h, h)
    first_sum = np.array([f(x) for x in support[1:-1]]).sum()
    second_sum = np.array([f((support[idx - 1] + support[idx]) / 2) for idx, _ in enumerate(support) if idx > 0]).sum()

    return (h / 3) * ((1 / 2) * f(a) + first_sum + 2 * second_sum + (1 / 2) * f(b))


def estimation_rechteck(a, b, tol, f, func_variable):
    h = (b - a) / n

    f_diff = sp.diff(f, func_variable, 2)
    f_diff_func = sp.lambdify(func_variable, f_diff, "numpy")

    max_pommes = np.array([np.abs(f_diff_func(x)) for x in np.linspace(a, b, 10000)]).max()

    h_pommes = np.sqrt((np.abs((24 * tol) / ((b - a) * max_pommes))))
    n_pommes = np.ceil((b - a) / h_pommes)

    return h_pommes, n_pommes


def estimation_trapez(a, b, tol, f, func_variable):
    f_diff = sp.diff(f, func_variable, 2)
    f_diff_func = sp.lambdify(func_variable, f_diff, "numpy")

    max_trapeze = np.array([np.abs(f_diff_func(x)) for x in np.linspace(a, b, 10000)]).max()

    h_trapeze = np.sqrt((np.abs((12 * tol) / ((b - a) * max_trapeze))))
    n_trapeze = np.ceil((b - a) / h_trapeze)

    return h_trapeze, n_trapeze


def estimation_simpson(a, b, tol, f, func_variable):
    f_diff = sp.diff(f, func_variable, 4)
    f_diff_func = sp.lambdify(func_variable, f_diff, "numpy")

    max_simpson = np.array([np.abs(f_diff_func(x)) for x in np.linspace(a, b, 10000)]).max()

    h_simpson = (np.abs((2880 * tol) / ((b - a) * max_simpson))) ** (1 / 4)
    n_simpson = np.ceil((b - a) / h_simpson)

    return h_simpson, n_simpson


if __name__ == '__main__':
    x = sp.symbols('x')

    a = 0
    b = 0.5
    tol = 1E-5

    f = sp.exp(-x ** 2)

    print(estimation_trapez(a, b, tol, f, x))

    f_func = sp.lambdify(x, f)

    n = 46
    print(sum_simpson_method(f_func, a, b, n))
