import sympy as sp

# a)
print()
print("a)")
x1, x2 = sp.symbols('x1 x2')
f1 = 5*x1*x2
f2 = x1**2 * x2**2 + x1 + 2*x2

print()
print('Functions: ')
print(f1)
print(f2)

# convert to matrix
f = sp.Matrix([f1,f2])
print(f)

X = sp.Matrix([x1,x2])
Df = f.jacobian(X)
print(Df)

# Werte einsetzen
print()
print('values of jacobian matrix: ')
Df0 = Df.subs([(x1,1),(x2,2)])
print(Df0)
print(Df0.evalf())

# b)
print()
print("b)")
x1, x2, x3 = sp.symbols('x1 x2 x3')
f1 = sp.ln(x1**2+x2**2) + x3**2
f2 = sp.exp(x2**2+x3**2) + x1**2
f3 = (1/(x3**2+x1**2)) + x2**2

print()
print('Functions: ')
print(f1)
print(f2)
print(f3)

# convert to matrix
f = sp.Matrix([f1,f2,f3])
print(f)

X = sp.Matrix([x1,x2,x3])
Df = f.jacobian(X)
print(Df)

# Werte einsetzen
print()
print('values of jacobian matrix: ')
Df0 = Df.subs([(x1,1),(x2,2),(x3,3)])
print(Df0)
print(Df0.evalf())

