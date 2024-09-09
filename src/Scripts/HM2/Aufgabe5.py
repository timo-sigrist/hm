import matplotlib.pyplot as plt
from matplotlib.pyplot import quiver
import numpy as np

def mittelpunkt(f, a, b, n, y0):
    h = (b - a) / n
    n = int(n + 1)
    y = np.zeros(n)
    x = np.linspace(a, b, int(n))
    y[0] = y0
    for i in range(n - 1):
        xh = x[i] + h / 2
        yh = y[i] + h / 2 * f(x[i], y[i])
        y[i + 1] = y[i] + h * f(xh, yh)
    return x, y

def richtungsfeld(f , xmin, xmax, ymin, ymax, hx, hy, useLinspace=False):
    xGrid = np.arange(xmin, xmax, hx)
    yGrid = np.arange(ymin, ymax, hy)
    # try with linspace if it doesn't work
    if useLinspace:
        xGrid = np.linspace(xmin, xmax, hx)
        yGrid = np.linspace(ymin, ymax, hy)
    X, Y = np.meshgrid(xGrid, yGrid)
    U = np.ones(X.shape)
    V = f(X, Y)
    # Richtungsfeld
    R = np.sqrt((abs(U) - len(X) / 2.0) ** 2 + (abs(V) - len(Y) / 2.0) ** 2)
    quiver(X, Y, U, V, R)

def modEuler(f, a, b, n, y0):
    h = (b - a) / n
    print("h", h)
    n = int(n + 1)
    y = np.zeros(n)
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    yi_euler = np.zeros(n)
    x = np.linspace(a, b, int(n))
    y[0] = y0
    for i in range(n - 1):
        yi_euler[i] = y[i] + h * f(x[i], y[i])
        print("yi_euler", yi_euler)
        k1[i] = f(x[i], y[i])
        k2[i] = f(x[i + 1], yi_euler[i])
        y[i + 1] = y[i] + h * (k1[i] + k2[i]) / 2
    print("k1", k1)
    print("k2", k2)
    print("y", y)
    return x, y

def f(x, y):
    return y - x

if __name__ == '__main__':
    # Aufgabe a)
    a = 0
    b = 1
    n = 10 # für 0.1 Schritte
    y0 = 2

    #Mittelpunkt
    x, y = mittelpunkt(f, a, b, n, y0)
    print(x)
    print(y)
    plt.scatter(x, y)
    plt.plot(x,y)
    plt.show()

    # Richungsfeld
    # x values
    xmin = 0
    xmax = 1
    xh = 0.1

    # y values
    ymin = 2
    ymax = 5
    yh = 0.1

    # Funktion der Steigung an jedem dieser Punkte
    f = lambda x, y: y-x

    # Erzeugung und Darstellung des Richtungsfeldes
    plt.title('Richtungsfeld')
    richtungsfeld(f, xmin, xmax, ymin, ymax, xh, yh)
    plt.show()


    #Aufgabe b)
    print("Mod Euler verfahren")
    x, y = modEuler(f, a, b, 1, 0)