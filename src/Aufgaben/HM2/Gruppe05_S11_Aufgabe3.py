from matplotlib.pyplot import show, plot, legend
from numpy import min, max

from Aufgaben.HM2.Richtungsfeld import richtungsfeld
from Eulerverfahren import euler, mittelpunkt, modEuler


def Name_S11_Aufg3(f, a, b, n, y0):
    # Euler-Verfahren
    x, y_euler = euler(f, a, b, n, y0)
    # Modifiziertes Euler-Verfahren
    x, y_modeuler = modEuler(f, a, b, n, y0)
    # Mittelpunkt-Verfahren
    x, y_mittelpunkt = mittelpunkt(f, a, b, n, y0)
    return x, y_euler, y_mittelpunkt, y_modeuler


if __name__ == "__main__":
    f = lambda x, y: x ** 2 / y
    a = 0
    b = 2.1
    y0 = 2
    h = 0.7
    n = int((b - a) / h)

    x, y_euler, y_mittelpunkt, y_modeuler = Name_S11_Aufg3(f,a,b,n,y0)

    # Graphen zeichnen
    plot(x, y_euler, label='Euler-Verfahren')
    plot(x, y_modeuler, label='Modifiziertes Euler-Verfahren')
    plot(x, y_mittelpunkt, label='Mittelpunkt-Verfahren')
    legend()

    # Richtungsfeld zeichnen
    ymin = min([y_euler, y_modeuler, y_mittelpunkt])
    ymax = max([y_euler, y_modeuler, y_mittelpunkt])
    richtungsfeld(f, a, b, ymin, ymax, 20, 20, True)
    show()
