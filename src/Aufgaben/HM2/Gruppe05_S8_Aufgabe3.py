import numpy as np


def f(_r, _rho):
    return _rho * 4 * np.pi * np.power(_r, 2)


def Gruppe5_S8_Aufg3a(x, y):
    Tf_neq = 0
    for i in range(len(x)-1):
        h = x[i+1]-x[i]
        Tf_neq += (y[i] + y[i+1])/2 * h
    return Tf_neq


if __name__ == '__main__':
    print("starting...")

    r = np.array([0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370], dtype=np.float64)
    rho = np.array([13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300], dtype=np.float64)
    earthMass = 5.972E24

    X = r * 1000
    Y = f(X, rho)
    tf_neq = Gruppe5_S8_Aufg3a(X, Y)

    print('calculated earth mass:', format(tf_neq, '.4e'))
    print('reference earth mass: ', earthMass)
    print('absolute error:', np.abs(tf_neq-earthMass))
    print('relative error [%]:', format(np.abs(tf_neq-earthMass)/earthMass * 100, '.2'))
