import numpy as np
from matplotlib import pyplot as plt
from Gruppe05_S8_Aufgabe1 import SumRf


# Gegeben Aufgabe a
def ai(t):
    return vrel * (µ / (ma - µ * t)) - g


def vi(t):
    return SumRf(ai, 0, t, n)


def hi(t):
    return SumRf(vi, 0, t, n)


# Gegeben Aufgabe b
def va(t):
    return vrel * np.log(ma / (ma - µ * t)) - g * t


def ha(t):
    return -vrel * (ma - µ * t) / µ * np.log(ma / (ma - µ * t)) + vrel * t - 0.5 * g * t ** 2


if __name__ == "__main__":
    a = 0
    b = 190
    n = 190
    g = 9.81
    vrel = 2600
    ma = 300000
    me = 80000
    te = 190
    µ = (ma - me) / te

    t = np.linspace(a, b, n)

    # Geschwindigkeit
    plt.plot(t, vi(t), '-.b', label="v(t) per Integral")
    plt.xlabel("t")
    plt.ylabel("v(t)")
    plt.plot(t, va(t), '--m', label="v(t) analytisch")
    plt.xlabel("t")
    plt.legend()
    plt.grid()

    plt.show()

    # Höhe
    plt.plot(t, hi(t), '-.b', label="h(t) per Integral")
    plt.xlabel("t")
    plt.ylabel("h(t)")
    plt.plot(t, ha(t), '--m', label="h(t) analytisch")
    plt.xlabel("t")
    plt.legend()
    plt.grid()

    plt.show()

    print('Resultate:')
    print('Geschwindigkeit |v]:\t%.2f' % vi(te))
    print('Höhe [m]:\t\t\t\t%.2f' % hi(te))
    print('Beschleunigung [g]:\t\t%.2f' % (ai(te) / g))
