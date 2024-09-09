import matplotlib.pyplot as plt
from numpy import dot, empty
from sympy import symbols, pprint, expand

def calc_lj(x, auslassen, x_int, n):
    li_oben = 1
    li_unten = 1
    for j in range(n):
        if j != auslassen:
            li_oben = li_oben * (x_int-x[j])
            li_unten = li_unten * (x[auslassen]-x[j])
    return li_oben/li_unten

def lagrange_int(x, y, x_int):
    n = len(x)
    y_int = 0

    for i in range(n):
        li = calc_lj(x, i, x_int, n)
        y_int += y[i] * li
    return y_int


x = [0, 2500, 5000, 10000]
y = [1013, 747, 540, 226]

# Wert für 3750
x1 = 3750
y1 = lagrange_int(x, y, x1)
print('')
print("Das Ergebnis der Lagrange-Interpolation für den Wert ", x1, "lautet: ", y1)

plt.scatter(x, y, label='Originalwerte')
plt.scatter(x1, y1, label='Zielwerte')
plt.legend()
plt.show()
