import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# a)
# Original Daten
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4])

# Erstellen der A-Matrix mit Ansatz:
# f(a, b, x) = a * T ** 2 + b * T + c
# np.array[...].T -A transformiert
A = np.array([x ** 2, x, np.ones(x.shape)]).T

# Lösen der Normalengleichung (direkt)"
lam = np.linalg.solve(A.T @ A, A.T @ y)

a = lam[0]
b = lam[1]
c = lam[2]

# mit QR Zerlegung
Q, R = np.linalg.qr(A)
lam2 = np.linalg.solve(R, Q.T@y)

a2 = lam2[0]
b2 = lam2[1]
c2 = lam2[2]


# b)
cond_ATA = np.linalg.cond(A.T @ A)
cond_R = np.linalg.cond(R)

print("cond(A.T@A) =", cond_ATA)
print("cond(R) =", cond_R)

# Resultat
# Die Konditionszahl der Matrix A.T@A ist viel grösser als diejenige der Matrix R.
# Daraus folgt:
# Die Matrix R ist besser konditioniert.
# Das beduetet, dass diese Fehler weniger als die Matrix A.T@A verstärkt.


# plotten
plt.plot(x, y, 'o', label='Daten')
t = np.linspace(x.min(), x.max())
plt.plot(t, a * t ** 2 + b * t + c, label='Normalengleichung direkt')
plt.plot(t, a2 * t ** 2 + b2 * t + c2, label='Mit QR-Zerlegung')

# c)
lamb_poly = np.polyfit(x, y, 2)
poly_y = np.polyval(lamb_poly, x)
plt.plot(x, poly_y, label='Mit Polyfit')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# d)
# 2. Norm
Ef = np.linalg.norm(y - A @ lam, 2) ** 2
Ef_QR = np.linalg.norm(y - A @ lam2, 2) ** 2
Ef_Polyfit = np.linalg.norm(y - A @ lamb_poly, 2) ** 2

print("E(f)\t\t=", Ef)
print("E(f_QR)\t\t=", Ef_QR)
print("E(f_Polyfit)\t=", Ef_Polyfit)

# Wir erhalten fast die gleichen Ergebnisse.
# Die Unterschiede liegen wohl in der Genauigkeit der einzelnen Methoden.
