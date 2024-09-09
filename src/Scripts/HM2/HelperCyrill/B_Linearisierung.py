from A_UtilityFunction import *

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')

sp.init_printing()

f1 = x1 ** 2 + x2 - 11
f2 = x1 + x2 ** 2 - 7

f = sp.Matrix([f1, f2])
x0 = sp.Matrix([1, 1])


# =============================================
# Start der Linearisierung
# =============================================

used_symbols = get_all_used_symbols(f)
X = sp.Matrix(used_symbols)

Df = f.jacobian(X)
print("Jacobi: ", Df)

subs_arg = []
for i in range(X.shape[0]):
    subs_arg.append((X[i], x0[i]))

f0 = f.subs(subs_arg)
print("Funktion mit Nullvektor: ", f0)

Df0 = Df.subs(subs_arg)
print("Jacobi mit Nullvektor: ", Df0)

print()
print("Resultat der Linearisierung: ")

g = f0 + Df0 * (X - x0)
print(g)

g_func = sp.lambdify([tuple(used_symbols)], g, "numpy")
print(g_func(x0))

