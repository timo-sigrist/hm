import sympy as sp

x = sp.Symbol('x')
# y = sp.Symbol('y')
# z = sp.Symbol('z')

# function = (1 / (z**2 + x**2)) + y**2
function = sp.sin(x)

print(f"Ableitung of ({function}) is:", sp.diff(function, x))

#für analytische Integration
print(f"Integration of ({function}) is:", sp.integrate(function, x))
integrateValue = sp.integrate(function,(x, 0, sp.pi))
print("Integration value is ", integrateValue)