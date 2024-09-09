import numpy as np
import matplotlib.pyplot as plt

x0 = np.pi / 3
relFehler = 0.1

def f(x):
    return x ** 2 * np.sin(x)


def f_ableitung(x):
    return 2 * x * np.sin(x) + x ** 2 * np.cos(x)


def K(x):
    return (np.absolute(f_ableitung(x) * np.absolute(x))) / (np.absolute(f(x)))

# x -> 0 konditioniert nach 3, deswegen gut konditioniert
print("Verhalten von konditionszahlen")
print([K(10 ** -n) for n in range(1, 6)])
print()

print("Näherungsweise absoluter Fehler")
konditionszahl_x0 = K(x0)
absFehler = relFehler / konditionszahl_x0 * np.absolute(x0)
print(absFehler)

# Ploten: (np.arrange(minimaler wert, maximaler wert, genauigkeit
plotrange = np.arange(-2 * np.pi, 3 * np.pi, 10 ** -4)

# semilogy = halblogarithmisch
plt.semilogy(plotrange, K(plotrange))
plt.xlabel('x')
plt.ylabel('K(x)')
plt.grid()
plt.show()
