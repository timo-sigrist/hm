import numpy as np
import matplotlib.pyplot as plt

from Normalgleichung_data import data

if __name__ == '__main__':
    TTank = data[:, 0]
    TBenzin = data[:, 1]
    pTank = data[:, 2]
    pBenzin = data[:, 3]
    y = data[:, 4]

    ones = np.ones(len(y))
    A = np.array([TTank, TBenzin, pTank, pBenzin, ones]).T

    l = np.linalg.solve(A.T @ A, A.T @ y)

    a = l[0]
    b = l[1]
    c = l[2]
    d = l[3]
    e = l[4]

    plt.title('Ausgleichsrechung mittels Normalgleichung')
    t = np.linspace(1971, 2003, len(y))
    plt.plot(t, y, 'o', label='Daten')
    plt.plot(t, a * TTank + b * TBenzin + c * pTank + d * pBenzin + e, label='Ausgleichsfunktion')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()