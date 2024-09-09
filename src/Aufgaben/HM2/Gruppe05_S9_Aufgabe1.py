import sympy as sp
import numpy as np

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

# Summierte RechteckRegel
def SumRfCond(_func, _a, _b, _genauigkeit):
    x = sp.Symbol('x')
    func_2_deriv = sp.diff(_func, x, 2)
    max = sp.Abs(sp.maximum(func_2_deriv, x, sp.Interval(a, b)))

    return sp.sqrt(func_2_deriv(max) * (_b - _a) * 24) / _genauigkeit


# TrapezRegel
def Tf(_func, _a, _b):
    return (_func(_a) + _func(_b)) / 2 * (_b - _a)


# Summierte TrapezRegel
def SumTf(_func, _a, _b, _n):
    sum = 0.
    h = (_b - _a) / _n
    # we don't do _n-1 because range() already stops at n-1
    for i in range(1, _n):
        x = _a + i*h
        sum += _func(x)
    return h * ((_func(_a) + _func(_b) / 2) + sum)


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


def Sf(_func, _a, _b):
    return 1/3 * (Tf(_func, _a, _b)+2*Rf(_func, _a, _b))


def f(x):
    return sp.log(x**2)


if __name__ == '__main__':
    x = sp.symbols("x")
    f_plain = sp.log(x**2)
    a = 1.
    b = 2.
    #h = ?
    #n = ?
    max_err = 10**-5

    integral = sp.integrate(f_plain, (x, a, b)).evalf()
    zweite_abl = sp.diff(f_plain, x, 2)
    vierte_abl = sp.diff(f_plain, x, 4)

    solved_a = abs(zweite_abl.evalf(subs={x:a}))
    solved_b = abs(zweite_abl.evalf(subs={x:b}))
    if solved_a > solved_b:
        maximum_zweite_abl = a
    else:
        maximum_zweite_abl = b

    solved_a = abs(vierte_abl.evalf(subs={x:a}))
    solved_b = abs(vierte_abl.evalf(subs={x:b}))
    if solved_a > solved_b:
        maximum_vierte_abl = a
    else:
        maximum_vierte_abl = b

    # Rechteck
    h = sp.sqrt(max_err * 24)
    n = np.ceil((b-a) / h)
    h = (b-a) / n
    Rf = SumRf(f, a, b, n)
    print(f"Summierte Rechtecksregel: {Rf}")
    print(f"Verifizierung: {abs(integral - Rf)}")
    print(f"Verifizierung: {h**2 / 24. * (b-a) * maximum_zweite_abl}")
    print(f"Verifizierung: {abs(integral - Rf) <= h**2 / 24. * (b-a) * maximum_zweite_abl}")
    print("-"*80)

    # Trapez
    h = sp.sqrt(max_err * 12)
    n = np.ceil((b-a) / h)
    h = (b-a) / n
    Tf = SumTf(f, a, b, n)
    print(f"Summierte Trapezregel: {Tf}")
    print(f"Verifizierung: {abs(integral - Tf)}")
    print(f"Verifizierung: {h**2 / 24. * (b-a) * maximum_zweite_abl}")
    print(f"Verifizierung: {abs(integral - Tf) <= h**2 / 12. * (b-a) * maximum_zweite_abl}")
    print("-"*80)

    # Simpson
    h = sp.root(max_err * 2880, 4)
    n = np.ceil((b-a) / h)
    h = (b-a) / n
    Sf = SumSf(f, a, b, n)
    print(f"Summierte Simpsonregel: {Sf}")
    print(f"Verifizierung: {abs(integral - Sf)}")
    print(f"Verifizierung: {h**4 / 2880. * (b-a) * maximum_vierte_abl}")
    print(f"Verifizierung: {abs(integral - Sf) <= h**4 / 2880. * (b-a) * maximum_vierte_abl}")
    print("-"*80)
