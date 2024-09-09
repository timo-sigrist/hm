import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import scipy.optimize
from sympy.utilities.lambdify import lambdify
from HM2_Serie07_Aufg2_Daten import x, y


def lambdify_func_to_array(input_symbols, func):
    # Lambdifies a given sympy functions and converts the output into a numpy-array
    func = lambdify([input_symbols], func)
    return lambda x: np.array(func(x))


def norm2_squared(vec):
    return np.linalg.norm(vec, 2) ** 2


def f_to_jacobian(f, x, y, parameters):
    X = sp.Matrix([y[i] - f(x[i], y[i]) for i in range(len(x))])
    Dg_sym = X.jacobian(parameters)
    Dg = lambdify_func_to_array(parameters, Dg_sym)
    g = lambdify_func_to_array(parameters, X)
    return Dg, g


# Ungedämpftes Gauss-Newton-Verfahren
def gauss_newton_undamped(Dg, g, lambda_init, tol_delta, delta=None):
    _n = 0

    if delta is None:
        delta = np.ones(lambda_init.shape[0])

    _lam = lambda_init

    while np.max(delta) >= tol_delta:
        _n += 1
        yn = g(_lam)
        A = -Dg(_lam)
        b = A.T@yn
        delta = np.linalg.solve(A.T@A, b).T[0]
        _lam = _lam + delta

    return _lam, _n


# Gedämpftes Gauss-Newton-Verfahren
def gauss_newton_damped(Dg, g, lambda_init, tol_delta, delta=None, pmax=10):
    _n = 0
    if delta is None:
        delta = np.ones(lambda_init.shape[0])

    _lam = lambda_init
    # Wiederhole die folgende Methode, solange die erforderliche Tolerant noch nicht erreicht ist.
    while np.max(delta) >= tol_delta:
        _n += 1
        yn = g(_lam)
        A = -Dg(_lam)
        b = A.T@yn
        delta = np.linalg.solve(A.T@A, b).T[0]

        p = 0
        lam_next = _lam + (delta / 2 ** p)

        # Wiederhole die folgende Methode, solange diese nicht besser als die vorherige ist.
        while norm2_squared(g(lam_next)) >= norm2_squared(g(_lam)) and p <= pmax:
            p += 1
            lam_next = _lam + (delta / 2 ** p)
            print('Dämpfung mit dem Wert p = ' + str(p))

        # Ist das erhaltene Resultat besser? Falls nicht, p = 0.
        if norm2_squared(g(lam_next)) >= norm2_squared(g(_lam)):
            lam_next = _lam + delta

        _lam = lam_next

    return _lam, _n


if __name__ == '__main__':
    # Startewerte, lam = lambda
    lam0 = np.array([100, 120, 3, -1]).T

    # Erforderliche Toleranz
    tol = 1E-5

    # Parameters to optimize (without x and y)
    # Parametersymbole in Sympy-Symbole umwandeln, Bezeichnungen stammen aus der Aufgabenstellung
    lamdba_0, lamdba_1, lamdba_2, lamdba_3 = sp.symbols('lamdba_0 lamdba_1 lamdba_2 lamdba_3')
    parameters = [lamdba_0, lamdba_1, lamdba_2, lamdba_3]

    # Function to optimize (without the y - f() part)
    # ACHTUNG: Formel muss auch noch in "Plotting" eingegeben werden."
    f = lambda x, y: (lamdba_0 + lamdba_1 * 10 ** (lamdba_2 + lamdba_3 * x)) / (1 + 10 ** (lamdba_2 + lamdba_3 * x))

    Dg, g = f_to_jacobian(f, x, y, parameters)

    # Undampened, lam = lambda
    lam, n = gauss_newton_undamped(Dg, g, lam0, tol)
    print('Ungedämpft: ' + str(lam) + ' mit n = ' + str(n))

    # Dampened, lam = lambda
    lam, n = gauss_newton_damped(Dg, g, lam0, tol)
    print('Gedämpft: ' + str(lam) + ' mit n = ' + str(n))

    # Plotting
    x_vals = np.arange(np.min(x), np.max(x), 0.01)
    # Falls der Ausdruck eine unzulässige Rechenopration ergibt (z. B. Diviosan durch 0),
    # muss das abgefangen werden.
    if (lambda x: 1 + 10 ** (lam[2] + lam[3] * x)) != 0:
        f = lambda x: (lam[0] + lam[1] * 10 ** (lam[2] + lam[3] * x)) / (1 + 10 ** (lam[2] + lam[3] * x))
    else:
        f = None

    plt.scatter(x, y)
    plt.plot(x_vals, f(x_vals))

    plt.show()

print('\nAlternative Berechnung der Parameter/Lambdas mit scipy.optimize')
def err_func(x):
    return np.linalg.norm(g(x)) ** 2

xopt = scipy.optimize.fmin(err_func, lam0)

print('xopt', xopt)

# Befund mit ungedämpften und gedämpften Newton
# Ungedämpft: [nan nan nan nan] mit n = 12
# Dämpfung mit dem Wert p = 1
# Gedämpft: [163.88257684 159.47423622   2.17221862  -0.42933895] mit n = 12

# Befund mit scipy.optimize
# Optimization terminated successfully.
#         Current function value: 0.591847
#         Iterations: 333
#         Function evaluations: 573
# xopt [163.88256553 159.47427156   2.17225694  -0.4293443 ]