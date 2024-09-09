import sympy as sp
import numpy as np

x1, x2, x3 = sp.symbols('x1 x2 x3')

f1 = x1 + x2**2 - x3**2 - 13
f2 = sp.ln(x2/4) + sp.exp(0.5*x3-1) - 1
f3 = (x2 - 3)**2 - x3**3 + 7

x0 = sp.Matrix([1.5, 3, 2.5])


# f
f = sp.Matrix([f1, f2, f3])

# X
X = sp.Matrix([x1, x2, x3])

# Df
Df = f.jacobian(X)

Df = sp.lambdify([x1, x2, x3], Df, 'numpy')
f = sp.lambdify([x1, x2, x3], f, 'numpy')

def norm(vec):
    return np.sqrt(vec[0]**2+vec[1]**2)

def calcXnPlus1(x0, xn, Df, f):
    print("xn:")
    print(xn)

    delta = np.linalg.solve(Df(np.float64(xn[0]), np.float64(xn[1]), np.float64(xn[2])), -f(np.float64(xn[0]), np.float64(xn[1]), np.float64(xn[2])))
    k = 0
    while np.linalg.norm(f(xn + delta/(2**k)) , 2) < np.linalg.norm(f(xn), 2):
        k = k+1

    delta = delta/2**k

    xnplus1 = xn + delta
    print("xnplus1:")
    print(xnplus1)
    return xnplus1

itr = 0
xn = x0
genauigkeit = 10e-5
normXnPlus1MinusXn = 1.0

while normXnPlus1MinusXn > genauigkeit:
    print()
    print("Itearation " + str(itr))
    print()
    itr += 1
    xnplus1 = calcXnPlus1(xn, Df, f)

    normXnPlus1MinusXn = norm(np.float64(xnplus1-xn))
    print("norm2 x(k)-x(k-1): " + str(normXnPlus1MinusXn))

    xn = xnplus1
