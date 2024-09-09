import numpy as np
from scipy.linalg import solve

A = np.array([
    (1,5,6),
    (7,9,6),
    (2,3,4)
], dtype=np.float64)

b = np.array([29,
              43,
              20], dtype=np.float64)

print("Result -> x:")
print (solve(A, b))