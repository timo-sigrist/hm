from pprint import pprint as pp
from sympy import Symbol

from newton import Newton
from simplified_newton import SimplifiedNewton
from secant_method import SecantMethod

sym = Symbol("x")
function = sym ** 2 - 2
count = 4
startvalue = 2

newton = Newton(sym, function, startvalue, count)
simplified_newton = SimplifiedNewton(sym, function, startvalue, count)

startvaluex0secante = 2
startvaluex1secante = -1.2
secant = SecantMethod(sym, function, startvaluex0secante, startvaluex1secante, count)

print("\n----- Newton: -----")
pp(newton.results)

print("\n----- Simplified Newton: -----")
pp(simplified_newton.results)

print("\n----- Secant Method: -----")
pp(secant.results)

secant = SecantMethod(sym, function, startvaluex0secante, startvaluex1secante, max_error=1e-6)
print("\n----- Secant Method Max Error: -----")
pp(secant.results)
print(secant.index)
