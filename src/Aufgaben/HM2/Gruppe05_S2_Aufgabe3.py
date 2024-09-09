import sympy as sp

x1, x2, x3 = sp.symbols('x1 x2 x3')
f1 = x1 + x2**2 - x3**2 - 13
f2 = sp.ln(x2/4) + sp.exp(0.5*x3-1) - 1
f3 = (x2 - 3)**2 - x3**3 + 7

# convert to matrix
f = sp.Matrix([f1,f2,f3])
X = sp.Matrix([x1,x2,x3])
Df = f.jacobian(X)

# Werte einsetzen
print()
print('values of f(x0): ')
f0 = f.subs([(x1,1.5),(x2,3),(x3,2.5)])
print(f0)
print()
print('values of Df(x0): ')
Df0 = Df.subs([(x1,1.5),(x2,3),(x3,2.5)])
print(Df0)
print()
X_minus_x0 = sp.Matrix([x1-1.5,x2-3,x3-2.5])

print('g: ')
g = f0 + Df0 * X_minus_x0
print(g)