import sympy as sp
import numpy as np

x1, x2 = sp.symbols('x1 x2')

f1 = 20 - 18*x1 - 2*x2**2
f2 = -4*x2 * (x1 - x2**2)
x0 = sp.Matrix([1.1, 0.9])

print("x0")
print(x0)

f = sp.Matrix([f1, f2])
print("f:")
print(f)


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

def norm(vec):
    return np.sqrt(vec[0]**2+vec[1]**2)

def calcXnPlus1(xn, Df, f):
    print("xn:")
    print(xn)

    delta = np.linalg.solve(Df(np.float64(xn[0]), np.float64(xn[1])), -f(np.float64(xn[0]), np.float64(xn[1])))
    print("delta:")
    print(delta)

    xnplus1 = xn + delta
    print("xnplus1:")
    print(xnplus1)

    normFXn = norm(np.float64(f(xn[0], xn[1])))
    print("Norm2 f(xn): " + str(normFXn))

    return xnplus1


itr = 0
xn = x0
while itr < 2:
    print()
    print("Itearation " + str(itr))
    print()
    itr += 1
    xnplus1 = calcXnPlus1(xn, Df, f)

    normXnPlus1MinusXn = norm(np.float64(xnplus1-xn))
    print("norm2 x(k)-x(k-1): " + str(normXnPlus1MinusXn))

    xn = xnplus1

