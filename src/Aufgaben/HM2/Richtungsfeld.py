from matplotlib.pyplot import quiver
from numpy import arange, linspace, meshgrid, ones, sqrt

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