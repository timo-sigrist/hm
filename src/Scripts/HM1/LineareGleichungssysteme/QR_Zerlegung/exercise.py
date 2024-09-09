import numpy as np

from QR_Zerlegung import QR_Zerlegung
from QR_Zerlegung import x_ausrechnen

A = np.array([
    [3, 1],
    [4, 1]
])
b = np.array([1, 2])

Q, R = QR_Zerlegung(A)
x_ausrechnen(Q, R, b)

