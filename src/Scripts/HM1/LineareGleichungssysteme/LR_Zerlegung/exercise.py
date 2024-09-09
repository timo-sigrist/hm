import numpy as np

from LR_Zerlegung import lrZerlegung
from MitPivotisierung import lrZerlegungMitPivotisierung

# Beispiel 4.4
A = np.array([
    [1, 2, -1],
    [4, -2, 6],
    [3, 1, 0]
])
b = np.array([9,-4,9])

# A = np.array([
#     (1,5,6),
#     (7,9,6),
#     (2,3,4)
# ])
# b = np.array([29,43,20])


# Beispiel 4.7
# A = np.array([
#     [3, 9, 12, 12],
#     [-2, -5, 7, 2],
#     [6, 12, 18, 6],
#     [3, 7, 38, 14]
# ])
#
# b = np.array(
#     [51, 2, 54, 79]
# )


### LR-Zerlegung ohne Pivotisierung ###
L,R,x,P = lrZerlegung(A,b)

### LR-Zerlegung mit Pivotisierung ###
#L,R,x,P = lrZerlegungMitPivotisierung(A,b)