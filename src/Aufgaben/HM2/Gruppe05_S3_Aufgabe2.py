import sympy as sp
import numpy as np

x, y = sp.symbols('x y')

f1 = x**2/186**2 - y**2/(300**2-186**2) - 1
f2 = (y-500)**2/279**2 - (x-300)**2/(500**2 - 279**2) - 1

#p1 = sp.plot_implicit(sp.Eq(f1, 0), (x, -2000, 2000), (y, -2000, 2000))
#p2 = sp.plot_implicit(sp.Eq(f2, 0), (x, -2000, 2000), (y, -2000, 2000))

#p1.append(p2[0])
#p1.show()

# Schätzwerte
# 1: -200, 200
# 2: 200, 200
# 3: 700, 900
# 4: -1200, 1500

genauigkeit = 10**-5

# Aufgabe b

x1, x2 = sp.symbols('x y')
# Pro Näherungsverktor laufen lassen
x0 = sp.Matrix([-200.0, 200.0])
#x0 = sp.Matrix([200.0, 200.0])
#x0 = sp.Matrix([700.0, 900.0])
#x0 = sp.Matrix([-1200.0, 1500.0])

# f
f = sp.Matrix([f1, f2])

# X
X = sp.Matrix([x1, x2])

# Df
Df = f.jacobian(X)

Df = sp.lambdify([x1, x2], Df, 'numpy')
f = sp.lambdify([x1, x2], f, 'numpy')

def norm(vec):
    return np.sqrt(vec[0]**2+vec[1]**2)

def calcXnPlus1(xn, Df, f):
    print("xn:")
    print(xn)

    delta = np.linalg.solve(Df(np.float64(xn[0]), np.float64(xn[1])), -f(np.float64(xn[0]), np.float64(xn[1])))

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
