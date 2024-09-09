import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Teilaufgabe a

year = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
percentage = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 75.7])

f = np.polyfit(year, percentage, len(year)-1)
pred_year = np.linspace(1981, 2010, (2010-1981)*10)
pred_percentage = np.polyval(f, pred_year)

fig = plt.figure(figsize=(10, 8))
plt.plot(pred_year, pred_percentage)
plt.title('Polyfit')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Geht das so berechnete Polynom wirklich exakt durch alle Datenpunkte?
# Nein, nur durch die berechneten.

# Teilaufgabe b

pred_year = np.linspace(1981, 2010, 2010-1981)
print("Schätzwert für das Jahr 2020:", np.polyval(f, pred_year))

# Teilaufgabe c

def calc_lj(x, auslassen, x_int, n):
    li_oben = 1.0
    li_unten = 1.0
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


print()
print("Schätzwert für das Jahr 2020:", lagrange_int(year, percentage, 2020))

# Ist das realistisch, und können solche Polynome hoher Ordnung für Schätzwerte ausserhalb des Intervalls der vorhandenen Datenwerte benutzt
# werden?
# Nein, sehr unrealistisch dass der Wert in 2020 -257277.57941781176 sein wird :)