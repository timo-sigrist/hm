import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from Gruppe05_S5_Aufgabe2 import cubic_spline


if __name__ == "__main__":
    x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
    y = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633, 281.422])
    xx = np.linspace(x.min(), x.max(), 100)
    plt.scatter(x, y)

    # Auswertung mit den Formeln gemäss der Unterrichtunterlagen
    spline_yy = cubic_spline(x, y, xx)
    plt.plot(xx, spline_yy, label='Splinefunktion')

    # Auswertung mit scipy
    cs = sp.interpolate.CubicSpline(x - x.min(), y)
    plt.plot(xx, cs(xx - xx.min()), label='Scipy')

    # Auswertung mit numpy
    polyfit = np.poly1d(np.polyfit(x - x.min(), y, 10))
    plt.plot(xx, polyfit(xx - xx.min()), label='Numpy')

    plt.legend()
    plt.show()
