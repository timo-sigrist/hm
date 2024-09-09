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

if __name__ == '__main__':
    #Aufgabe a)
    # nicht lineares Gleichungssystem
    a, b, c = sp.symbols('a b c')
    f1 = (sp.sqrt(sp.exp(a)) + sp.log(6110.38**b) + c**2*(sp.log(6110.38))**3) * 283.15
    f2 = (sp.sqrt(sp.exp(a)) + sp.log(3833.33**b) + c**2*(sp.log(3833.33))**3) * 293.15
    f3 = (sp.sqrt(sp.exp(a)) + sp.log(2470.6**b) + c**2*(sp.log(2470.6))**3) * 303.15

    # Aufgabe b)

    #Die Lösung ist x10: [[-18.9999999998979], [3.04487826986382e-16], [0.000976562499999875]]

    # Startvektor
    x1_start, x2_start, x3_start = 1,1,1

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
    genauigkeit = 10e-2
    normXnPlus1MinusXn = 1.0

    xn = x0

    # while normXnPlus1MinusXn > genauigkeit:
    while itr < 10:
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