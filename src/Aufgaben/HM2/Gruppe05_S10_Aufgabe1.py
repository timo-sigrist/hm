from numpy import zeros


def romberg_extrapolation(f, a, b, m: int):
    m += 1
    T = zeros([m, m])
    for j in range(m):
        h = (b - a) / 2 ** j
        n = (b - a) / h
        T[j, 0] = SumTf(f, a, b, int(n))
    for k in range(1, m):
        for i in range(0, (m - k)):
            T[i, k] = (4 ** k * T[i + 1, k - 1] - T[i, k - 1]) / (4 ** k - 1)
    return T


def SumTf(f, a, b, n: int):
    area = 0
    h = (b - a) / n
    xi = a
    for i in range(1, n + 1):
        area += (((f(xi) + f(xi + h)) / 2) * h)
        xi = xi + h
    return area

# Gegeben
a = 0
b = 100
m = 5

# a)
f = lambda x: -97000 / (-5 * x ** 2 - 570000)
print(romberg_extrapolation(f, a, b, m))
# Das Flugzeug benötigt zirka 16.54 Sekunden bis zum Stillstand.

# b)
f = lambda x: -97000 * x / (-5 * x ** 2 - 570000)
print(romberg_extrapolation(f, a, b, m))
# Das Flugzeug benötigt zirka 815.48 m bis zum Stillstand.
