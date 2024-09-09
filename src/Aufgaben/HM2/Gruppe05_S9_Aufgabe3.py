import numpy as np
from Gruppe05_S8_Aufgabe1 import SumTf

# Beispiel 7.2
# def f(x):
#     return 1. / x


def f(x):
    return np.cos(x**2)


def Romberg(_f, _a, _b, _m):
    t_j_k = [[]]

    for i in range(_m + 1):
        n_i = 2**i
        h_i = (_b - _a) / n_i
        t_j_k[0].append(h_i * ((_f(_a) + _f(_b)) / 2. + sum(_f(_a + j * h_i) for j in range(1, n_i))))
        # print(f"T_{i}0 = {t_j_k[0][i]}")

    for k in range(1, _m + 1):
        for j in range(_m - k + 1):
            if len(t_j_k) != k + 1:
                t_j_k.append([])
            t_j_k[k].append((4**k * t_j_k[k - 1][j + 1] - t_j_k[k - 1][j]) / (4**k - 1))
            print(f"T{j}{k-1}: {t_j_k[k-1][j]}")
        print(f"T{j+1}{k-1}: {t_j_k[k-1][j+1]}")

    return t_j_k[-1]


if __name__ == "__main__":
    # Beispiel 7.2 aus dem Skript
    # print(Romberg(f, 2., 4., 3))

    # Aufgabe 2
    print(Romberg(f, 0, np.pi, 4))
