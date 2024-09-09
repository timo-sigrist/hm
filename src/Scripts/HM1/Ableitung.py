import sympy as sp

x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')

function = (1 / (z**2 + x**2)) + y**2

print(f"Ableitung of ({function}) is:", sp.diff(function, x))
