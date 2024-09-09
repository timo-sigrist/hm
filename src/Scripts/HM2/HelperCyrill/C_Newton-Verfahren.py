from A_UtilityFunction import *
import sympy as sp
import numpy as np
import itertools

def init_newton(f, x0):
    X = sp.Matrix(get_all_used_symbols(f))
    expr = tuple([v] for i, v in enumerate(X))

    f_func = sp.lambdify([expr], f, "numpy")

    Df = f.jacobian(X)
    Df_func = sp.lambdify([expr], Df, "numpy")

    print("nichtlineare Gleichungssystem", f)
    print("Jacobi Matrix", Df)

    print("Schritt: ", 0)
    print(x0)

    return f_func, Df_func


def newton_method(f, x0, accuracy=None, max_steps=None):
    # =============================================
    # Start Newton Verfahren
    # =============================================
    f_func, Df_func = init_newton(f, x0)

    x = x0
    for i in itertools.count(0):
        delta = np.linalg.solve(Df_func(x[i]), -f_func(x[i]))
        x_next = x[i] + delta

        x.append(x_next)
        print("Schritt: ", i + 1, x_next)

        if max_steps is not None and i + 1 >= max_steps:
            return x

        if accuracy is not None and np.linalg.norm(x[i + 1] - x[i]) < accuracy:
            return x


def simplified_newton_method(f, x0, accuracy=None, max_steps=None):
    # =============================================
    # Start vereinfachter Newton Verfahren
    # =============================================
    f_func, Df_func = init_newton(f, x0)

    Df_value = Df_func(x0)
    x = [x0]
    for i in itertools.count(0):
        delta = np.linalg.solve(Df_value, -f_func(x[i]))
        x_next = x[i] + delta

        x.append(x_next)
        print("Schritt: ", i + 1, x_next)

        if max_steps is not None and i + 1 >= max_steps:
            return x

        if accuracy is not None and np.linalg.norm(x[i + 1] - x[i]) < accuracy:
            return x


def damped_newton_method(f, x0, max_k, accuracy=None, max_steps=None):
    # =============================================
    # Start gedämpfter Newton Verfahren
    # =============================================
    f_func, Df_func = init_newton(f, x0)

    x = [x0]
    for i in itertools.count(0):
        delta = np.linalg.solve(Df_func(x[i]), -f_func(x[i]))

        damp = 1
        for k in range(0, max_k + 1):
            if np.linalg.norm(f_func(x[i] + (delta / (2 ** k))), 2) < np.linalg.norm(f_func(x[i]), 2):
                damp = 1 / (2 ** k)

                print("(", i + 1, ") ", "damp: ", damp, "| steps: ", k)
                break

        x_next = x[i] + delta * damp

        x.append(x_next)
        print("Schritt: ", i + 1, x_next)

        if max_steps is not None and i + 1 >= max_steps:
            return x

        if accuracy is not None and np.linalg.norm(x[i + 1] - x[i]) < accuracy:
            return x


if __name__ == "__main__":
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')

    sp.init_printing()

    f1 = 2 * x1 + 4 * x2
    f2 = 4 * x1 + 8 * x2 ** 3

    f = sp.Matrix([f1, f2])
    x0 = np.array([4, 2]).reshape(-1, 1)

    accuracy = None
    max_steps = 5
    max_k = 4

    print(newton_method(f, x0, accuracy, max_steps))
    print(simplified_newton_method(f, x0, accuracy, max_steps))
    print(damped_newton_method(f, x0, max_k, accuracy, max_steps))