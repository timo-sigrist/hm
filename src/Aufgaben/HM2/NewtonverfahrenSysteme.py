import sympy as sp
import numpy as np

x1, x2 = sp.symbols('x1 x2')

f1 = 20 - 18*x1 - 2*x2**2
f2 = -4*x2 * (x1 - x2**2)

f = sp.Matrix([f1, f2])
print("f:")
print(f)

x0 = sp.Matrix([1.1, 0.9])
print("x0")
print(x0)

# X
X = sp.Matrix([x1, x2])
print("X:")
print(X)

# Df
Df = f.jacobian(X)
print("Jacobi-Matrix:")
print(Df)

Df = sp.lambdify([x1, x2], Df, 'numpy')
f = sp.lambdify([x1, x2], f, 'numpy')

def calcXnPlus1(xn, Df,  f):
    print("xn")
    print(xn)

    delta = np.linalg.solve(Df(np.float64(xn[0]), np.float64(xn[1])), -f(np.float64(xn[0]), np.float64(xn[1])))

    print("delta:")
    print(delta)

    xnplus1 = xn + delta
    print("xnplus1")
    print(xnplus1)

    return xnplus1

itr = 0
xn = x0
while itr < 2:
    print()
    print("Itearation " + str(itr))
    print()
    itr += 1
    xn = calcXnPlus1(xn, Df, f)

