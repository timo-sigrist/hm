import numpy as np
import matplotlib.pyplot as plt

def cubic_spline(x, y, xx):
    # Check if all values are contained in allowed range
    # Number of x-values, which equals the number of steps in which the range
    # between the smallest and larges x-values are devided.
    ilen = len(xx)
    # Extracts all x-values, which are <= than the first x-value
    xx = np.extract(x[0] <= xx, xx)
    # Extracts all x-values, which are >= than the last x-value
    xx = np.extract(x[len(x) - 1] >= xx, xx)
    if len(xx) != ilen:
        raise Exception('Es sind nicht alle x-Werte im erforderlichen Bereich.')

    # Set a-values equal to y-values, thus defining the a coefficients
    a = y

    # Define number of i
    i = len(x) - 1

    # Calculate h-values as difference of each value, i.e. x[1] - x[0], x[2] - x[1] and so on
    h = np.diff(x)

    A = np.zeros(shape=(i-1, i-1))
    z = np.zeros(shape=(i-1, 1))
    for j in range(0, i-1):
        A[j, j] = 2 * (h[j] + h[j+1])
        if j != i-2:
            A[j+1, j] = h[j+1]
            A[j, j+1] = h[j+1]

        z[j, 0] = 3 * (y[j+2]-y[j+1]) / h[j] - 3 * (y[j+1]-y[j]) / h[j]

    c = np.zeros(shape=(i+1, 1))
    c_copy = np.linalg.solve(A, z)
    for j in range(1, len(c_copy)+1):
        c[j, 0] = c_copy[j-1, 0]

    b = np.zeros(len(x), dtype=float)
    d = np.zeros(len(x), dtype=float)
    for j in range(0, i):
        b[j] = ((y[j+1]-y[j]) / h[j]) - ((h[j]/3) * (c[j+1, 0] + 2*c[j, 0]))
        d[j] = (1 / (3*h[j])) * (c[j+1] - c[j])

    yy = np.zeros(0)
    for i in range(i + 1):
        S = lambda xs: np.polyval([d[i], c[i], b[i], a[i]], xs - x[i])
        xs = np.extract(x[i] <= xx, xx)
        if i != len(x) - 1:
            xs = np.extract(xs < x[i + 1], xs)
        yy = np.concatenate((yy, S(xs)))

    # return a, b, c, d
    return yy


if __name__ == "__main__":
    x = np.array([4, 6, 8, 10])
    y = np.array([6, 3, 9, 0])
    xx = np.linspace(x.min(), x.max(), 100)
    spline_yy = cubic_spline(x, y, xx)
    plt.scatter(x, y)
    plt.plot(xx, spline_yy, label='Splinefunktion')
    plt.legend()
    plt.show()
