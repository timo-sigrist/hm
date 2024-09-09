import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from HM2_Serie06_Aufg3_Daten import data

x = data[:, 0]
y = data[:, 1]

log10_y = np.log10(y)
A = np.array([x - 1970, np.ones(x.shape)]).T

l = np.linalg.solve(A.T @ A, A.T @ log10_y)

a = l[0]
b = l[1]

#Mooresches Gesetz
N_null = 2250
t_calculated = np.arange(1970, 2020, 1)
moore_maximal = N_null * 2.0 ** ((t_calculated - 1971) / 1.5)
moore_minimal = N_null * 2.0 ** ((t_calculated - 1971) / 2.0)

plt.title('Anzahl Transistoren in Prozessor-Chips')
plt.scatter(x, log10_y, label="Messwerte")
plt.scatter([2015], [4 * 10 ** 9], label="Tatsächliche Anzahl" )

plt.semilogy(t_calculated, moore_maximal, label="Moore Max")
plt.semilogy(t_calculated, moore_minimal, label="Moore Min")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
