import sympy as sp
import numpy as np

def norm(vec):
    return np.sqrt(vec[0]**2+vec[1]**2)

def newton(xn, Df, f, itr):
    print("x" + str(itr) + ":")
    print(xn)

    delta = np.linalg.solve(Df(np.float64(xn[0]), np.float64(xn[1]), np.float64(xn[2])), -f(np.float64(xn[0]), np.float64(xn[1]), np.float64(xn[2])))

    print("delta:")
    print(delta)

    xnplus1 = xn + delta
    print("x" + str(itr+1) + ":")
    print(xnplus1)

    return xnplus1

def newton_vereinfacht(x0, xn, Df, f, itr):
    print("x" + str(itr) + ":")
    print(xn)

    delta = np.linalg.solve(Df(np.float64(x0[0]), np.float64(x0[1]), np.float64(x0[2])), -f(np.float64(xn[0]), np.float64(xn[1])))

    print("delta:")
    print(delta)

    xnplus1 = xn + delta
    print("x" + str(itr+1) + ":")
    print(xnplus1)

    return xnplus1

# def norm2_squared(vec):
#     return np.linalg.norm(vec, 2) ** 2
#
# def newton_gedämpft(x0, xn, Df, f, itr, pmax=10):
#     print("x" + str(itr) + ":")
#     print(xn)
#
#     delta = np.linalg.solve(Df(np.float64(xn[0]), np.float64(xn[1])), -f(xn))
#
#     p = 0
#     lam_next = x0 + (delta / 2 ** p)
#
#     # Wiederhole die folgende Methode, solange diese nicht besser als die vorherige ist.
#     while norm2_squared(f(lam_next)) >= norm2_squared(f(x0)) and p <= pmax:
#         p += 1
#         lam_next = x0 + (delta / 2 ** p)
#         print('Dämpfung mit dem Wert p = ' + str(p))
#
#     print("delta:")
#     print(delta)
#
#     xnplus1 = xn + delta
#     print("x" + str(itr+1) + ":")
#     print(xnplus1)
#
#     return xnplus1

if __name__ == '__main__':
    # Funktionen
    a, b, c = sp.symbols('a b c')
    f1 = a + b * sp.exp(c*1) - 40
    f2 = a + b * sp.exp(c*1.6) - 250
    f3 = a + b * sp.exp(c*2) - 800

    # Startvektor
    x1_start, x2_start, x3_start = 1,2,3

    f = sp.Matrix([f1, f2, f3])
    print("f:")
    print(f)

    x0 = sp.Matrix([x1_start, x2_start, x3_start])
    print("x0")
    print(x0)

    # X
    X = sp.Matrix([a, b, c])
    print("X:")
    print(X)

    # Df
    Df = f.jacobian(X)
    print("Jacobi-Matrix:")
    print(Df)

    Df = sp.lambdify([a, b, c], Df, 'numpy')
    f = sp.lambdify([a, b, c], f, 'numpy')
    # f = lambda x, y, z: np.array(f(x,y,z))

    # Iterativ oder Genauigkeit
    itr = 0
    genauigkeit = 10e-5
    normXnPlus1MinusXn = 1.0

    xn = x0

    # while normXnPlus1MinusXn > genauigkeit:
    while itr < 1:
        print()
        print("Itearation " + str(itr))
        print()
        # normal oder vereinfacht
        xnplus1 = newton(xn, Df, f, itr)
        # xnplus1 = newton_vereinfacht(x0, xn, Df, f, itr)
        # xnplus1 = newton_gedämpft(x0, xn, Df, f, itr)

        normXnPlus1MinusXn = norm(np.float64(xnplus1 - xn))

        xn = xnplus1

        itr += 1
        print('------------------------------------------')

    print('Es brauchte ' + str(itr) + ' Iterationen')