import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from HM2_Serie06_Aufg2_Daten import data

TTank = data[:, 0]
TBenzin = data[:, 1]
pTank = data[:, 2]
pBenzin = data[:, 3]
mch = data[:, 4]

ones = np.ones(len(mch))

A = np.array([TTank, TBenzin, pTank, pBenzin, ones]).T

l = np.linalg.solve(A.T @ A, A.T @ mch)


a = l[0]
b = l[1]
c = l[2]
d = l[3]
e = l[4]

plt.title('Enasse der entwichenen Dämpfe')
t = np.linspace(30, 100, len(mch))
plt.plot(t, mch, 'o', label='Daten')
plt.plot(t, a * TTank + b * TBenzin + c * pTank + d * pBenzin + e, label='Ausgleichsfunktion')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


