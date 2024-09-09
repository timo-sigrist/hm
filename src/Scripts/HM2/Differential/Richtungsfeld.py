from matplotlib.pyplot import quiver
import matplotlib.pyplot as plt
from numpy import arange, linspace, meshgrid, ones, sqrt, sin

def richtungsfeld(f , xmin, xmax, ymin, ymax, hx, hy, useLinspace=False):
    xGrid = arange(xmin, xmax, hx)
    yGrid = arange(ymin, ymax, hy)
    # try with linspace if it doesn't work
    if useLinspace:
        xGrid = linspace(xmin, xmax, hx)
        yGrid = linspace(ymin, ymax, hy)
    X, Y = meshgrid(xGrid, yGrid)
    U = ones(X.shape)
    V = f(X, Y)
    # Richtungsfeld
    R = sqrt((abs(U) - len(X) / 2.0) ** 2 + (abs(V) - len(Y) / 2.0) ** 2)
    quiver(X, Y, U, V, R)


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
