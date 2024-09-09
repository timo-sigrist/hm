import numpy as np
import matplotlib.pyplot as plt

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

if __name__ == '__main__':
    # Geht das so berechnete Polynom wirklich exakt durch alle Datenpunkte?
    # Nein, nur durch die berechneten.

    x = np.array([0, 2500, 5000, 10000])
    y = np.array([1013, 747, 540, 226])

    f = np.polyfit(x, y, len(x) - 1)

    # x_to_predict = np.linspace(8, 14, (14 - 8))
    x_to_predict = 12000

    print('np.polyval:')
    y_predicted = np.polyval(f, x_to_predict)
    print("Schätzwert für " + str(x_to_predict) + " :", y_predicted)
    print()
    print('lagrange_int:')
    y_predicted = lagrange_int(x, y, x_to_predict)
    print("Schätzwert für " + str(x_to_predict) + " :", y_predicted)

    fig = plt.figure(figsize=(10, 8))
    plt.plot(x, y)
    plt.title('Polyfit')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()