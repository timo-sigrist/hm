# Numerische Integration
import numpy as np
import sympy as sp

# RechteckRegel
def Rf(_func, _a, _b):
    return _func((_a + _b) / 2) * (_b - _a)


# Summierte RechteckRegel
def SumRf(_func, _a, _b, _n):
    sum = 0.
    h = (_b - _a) / _n
    # we don't do _n-1 because range() already stops at n-1
    for i in range(0, _n):
        x = _a + i*h
        sum += _func(x + h/2)
    return h * sum

# TrapezRegel
def Tf(_func, _a, _b):
    return (_func(_a) + _func(_b)) / 2 * (_b - _a)


# Summierte TrapezRegel
def SumTf(_func, _a, _b, _n: int):
    area = 0
    h = (_b - _a) / _n
    xi = _a
    for i in range(1, _n + 1):
        area += (((_func(xi) + _func(xi + h)) / 2) * h)
        xi = xi + h
    return area


# SimpsonRegel
def Sf(_func, _a, _b):
    return 1/3 * (Tf(_func, _a, _b)+2*Rf(_func, _a, _b))

# Summierte SimpsonRegel
def SumSf(_func, _a, _b, _n):
    sumTf = 0.
    sumRf = 0.
    h = (_b - _a) / _n
    # sumTf
    for i in range(1, _n):
        x = _a + i*h
        sumTf += _func(x)
    # sumRf
    for i in range(1, _n+1):
        x = _a + i*h
        x_minus_one = _a + (i-1)*h
        sumRf += _func((x_minus_one + x) / 2)

    return h/3 * (1/2 * _func(_a) + sumTf + 2*sumRf + 1/2 * _func(_b))

def SumRFTol(a, b, tol, f, func_variable):

    f_diff = sp.diff(f, func_variable, 2)
    f_diff_func = sp.lambdify(func_variable, f_diff, "numpy")

    max_pommes = np.array([np.abs(f_diff_func(x)) for x in np.linspace(a, b, 10000)]).max()

    h_pommes = np.sqrt((np.abs((24 * tol) / ((b - a) * max_pommes))))
    n_pommes = np.ceil((b - a) / h_pommes)

    print("estimated h", h_pommes)
    print("estimated n", n_pommes)

    funclam = sp.lambdify(func_variable, f)
    resSumRecht = SumRf(funclam, a, b, int(n_pommes)) # mit dem resultaten aus estimate weiterrechnen
    print("Res Rechteck", resSumRecht)

    return resSumRecht

def SumTFTol(a, b, tol, f, func_variable):
    f_diff = sp.diff(f, func_variable, 2)
    f_diff_func = sp.lambdify(func_variable, f_diff, "numpy")

    max_trapeze = np.array([np.abs(f_diff_func(x)) for x in np.linspace(a, b, 10000)]).max()

    h_trapeze = np.sqrt((np.abs((12 * tol) / ((b - a) * max_trapeze))))
    n_trapeze = np.ceil((b - a) / h_trapeze)
    print("estimated h", h_trapeze)
    print("estimated n", n_trapeze)

    funclam = sp.lambdify(func_variable, f)
    resSumTrap = SumTf(funclam, a, b, int(n_trapeze)) # mit dem resultaten aus estimate weiterrechnen
    print("Res Trapez", resSumTrap)

    return resSumTrap


def SumSFTol(a, b, tol, f, func_variable):
    f_diff = sp.diff(f, func_variable, 4)
    f_diff_func = sp.lambdify(func_variable, f_diff, "numpy")

    max_simpson = np.array([np.abs(f_diff_func(x)) for x in np.linspace(a, b, 10000)]).max()

    h_simpson = (np.abs((2880 * tol) / ((b - a) * max_simpson))) ** (1 / 4)
    n_simpson = np.ceil((b - a) / h_simpson)

    print("estimated h", h_simpson)
    print("estimated n", n_simpson)

    funclam = sp.lambdify(func_variable, f)
    resSumSf = SumSf(funclam, a, b, int(n_simpson)) # mit dem resultaten aus estimate weiterrechnen
    print("Res Trapez", resSumSf)

    return resSumSf


def f(x):
    return np.exp(-x**2)

if __name__ == '__main__':
    # print("starting...")
    # n = 5
    # m = 10
    b = 2  # stop
    a = 1  # start
    tol = 1e-5

    # normal
    # via_rechteck = SumRf(f, a, b, n)
    # via_trapez = SumTf(f, a, b, n)
    # via_simpson = SumSf(f, a, b, n)

    # mit genauigkeit
    x = sp.symbols("x")
    func = sp.ln(x**2)
    SumRFTol(a,b, tol, func, x)
    SumTFTol(a,b, tol, func, x)
    SumSFTol(a, b, tol, func, x)
