from A_UtilityFunction import *

import numpy as np
import itertools

a, b = sp.symbols('a b')
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')


def linear_normal_equation_system(x, y):
    # =============================================
    # Start lineare Normalgleichungssystem
    # (löst nur lineare Ausgleichsprobleme)
    # =============================================

    A = np.array([x, np.ones(x.shape)]).T
    Q, R = np.linalg.qr(A)

    qr_res = np.linalg.solve(R, Q.T@y)

    print(qr_res)


def init_gauss_newton(f, x, y):
    X = sp.Matrix([a, b])
    expr = tuple([v] for i, v in enumerate(X))

    g = sp.Matrix([y[i] - f.subs(x1, x[i]) for i in range(x.size)])
    Dg = g.jacobian(X)

    g_func = sp.lambdify([expr], g, "numpy")
    Dg_func = sp.lambdify([expr], Dg, "numpy")

    return g_func, Dg_func


def gauss_newton_method(f, x, y, lam0, accuracy=None, max_steps=None):
    # =============================================
    # Start Gauss-Newton Verfahren
    # =============================================
    g_func, Dg_func = init_gauss_newton(f, x, y)

    lam = [lam0]
    for i in itertools.count(0):
        Q, R = np.linalg.qr(Dg_func(lam[i]))
        delta = np.linalg.solve(R, -Q.T @ g_func(lam[i]))

        lam_next = lam[i] + delta

        lam.append(lam_next)
        print("Schritt: ", i + 1, lam_next)

        if max_steps is not None and i + 1 >= max_steps:
            return lam

        if accuracy is not None and np.linalg.norm(lam[i + 1] - lam[i]) < accuracy:
            return lam


def damped_gauss_newton_method(f, x, y, lam0, max_p, accuracy=None, max_steps=None):
    # =============================================
    # Start gedämpfter Gauss-Newton Verfahren
    # =============================================
    g_func, Dg_func = init_gauss_newton(f, x, y)

    lam = [lam0]
    for i in itertools.count(0):
        Q, R = np.linalg.qr(Dg_func(lam[i]))
        delta = np.linalg.solve(R, -Q.T @ g_func(lam[i]))

        damp = 1
        for p in range(0, max_p + 1):
            if np.linalg.norm(g_func(lam[i] + delta / (2 ** p)), 2) ** 2 < np.linalg.norm(g_func(lam[i]), 2) ** 2:
                damp = (2 ** p)

                print("(", i + 1, ") ", "damp: ", damp, "| steps: ", p)
                break

        lam_next = lam[i] + delta / damp

        lam.append(lam_next)
        print("Schritt: ", i + 1, lam_next)

        if max_steps is not None and i + 1 >= max_steps:
            return lam

        if accuracy is not None and np.linalg.norm(delta / damp, 2) < accuracy:
            return lam


if __name__ == '__main__':
    x = np.array([1, 2, 3, 4])
    y = np.array([6, 6.8, 10, 10.5])

    linear_normal_equation_system(x, y)

    f = a * sp.exp(b * x1)

    x = np.array([0, 1, 2, 3, 4])
    y = np.array([3, 1, 0.5, 0.2, 0.05])
    lam0 = np.array([1, -1.5]).reshape(-1, 1)

    tol = 1E-8
    max_iter = 30
    max_p = 5

    print(gauss_newton_method(f, x, y, lam0, tol, max_iter))
    print(damped_gauss_newton_method(f, x, y, lam0, max_p, tol, max_iter))
