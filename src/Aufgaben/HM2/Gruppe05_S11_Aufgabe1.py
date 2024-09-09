import matplotlib.pyplot as plt
from numpy import sin
from Richtungsfeld import richtungsfeld


if __name__ == "__main__":
    # x values
    xmin = -5
    xmax = 5
    xh = 0.5

    # y values
    ymin = -5
    ymax = 5
    yh = 0.5

    # Funktion der Steigung an jedem dieser Punkte
    f = lambda x, y: sin(x * y * 0.4)

    # Erzeugung und Darstellung des Richtungsfeldes
    plt.title('Richtungsfeld')
    richtungsfeld(f, xmin, xmax, ymin, ymax, xh, yh)
    plt.show()
