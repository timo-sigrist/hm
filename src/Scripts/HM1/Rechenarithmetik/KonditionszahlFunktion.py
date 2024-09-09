import numpy as np
import matplotlib.pyplot as plt

# Bsp vom aktuellen Code ist die funktion des Quadrieren f(x): x^2

# TODO edit f(x) and f_ableitung(x) and set x values

x = np.arange(-4, 2, 0.05)
#x = np.array([5])


def f(x):
    return x ** 2


def f_ableitung(x):
    return 2 * x


# Konditionszahl
#          f'(x)*x
# K(x) = |---------|
#            f(x)

def K(x):
    return (np.abs(f_ableitung(x)) * np.abs(x)) / np.abs(f(x))


nr_fuer_gut_konditioniert = 1
xk_gut_konditioniert = []
for x_wert in x:
    if K(x_wert) <= nr_fuer_gut_konditioniert:
        xk_gut_konditioniert.append(x_wert)

print("Alle X für K <=" + str(nr_fuer_gut_konditioniert) + ": \n " + str(xk_gut_konditioniert))
if xk_gut_konditioniert:
    print("X ist gut Konditioniert für Min: " + str(min(xk_gut_konditioniert)) + ", Max: " + str(max(xk_gut_konditioniert)) )

# plott halblogarithmisch im Bereich....
# plt.semilogy(x,K(x))
plt.plot(x, K(x), '-'), plt.xlabel('x'), plt.ylabel('K(x)')
plt.show()
print("Alle Konditionszahlen: \n" + str(K(x)))
