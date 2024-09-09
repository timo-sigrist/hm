# Numerische Integration
import numpy as np
import sympy as sp

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

def romberg_extrapolation(f, a, b, m: int):
    m += 1
    T = np.zeros([m, m])
    for j in range(m):
        h = (b - a) / 2 ** j
        n = (b - a) / h
        T[j, 0] = SumTf(f, a, b, int(n))
    for k in range(1, m):
        for i in range(0, (m - k)):
            T[i, k] = (4 ** k * T[i + 1, k - 1] - T[i, k - 1]) / (4 ** k - 1)
    return T

def f(t):
    return t**2 * (1-t)**2


if __name__ == '__main__':
    #Aufgabe a)
    t = sp.Symbol('t')
    function = t * (1-t)
    integrateValue = sp.integrate(function,(t, 0, 1))
    print("Analytische Wert für p(1) ist ", integrateValue)

    a = 0  # start
    b = 1  # stop
    tol = 1e-6
    SumTFTol(a,b, tol, function, t)

    #Aufgabe b)
    print("Romberg extrapolation")
    print(romberg_extrapolation(f, 0, 1, 3))

