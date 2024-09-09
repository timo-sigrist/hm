import numpy as np


def ist_diagonaldominant(A):
    a_xy = 0
    b_xy = 0
    diagonaldominant = bool(True)
    n = A.shape[0]
    for y in range(0, n):
        row_sum = 0
        for x in range(0, n):
            if x == y:
                a_xy = abs(A[y][x])
            else:
                row_sum += abs(A[y][x])
            if row_sum > a_xy:
                diagonaldominant = False
    if diagonaldominant == False:
        diagonaldominant = bool(True)
        for y in range(0, n):
            column_sum = 0
            #b_xy = 0
            print(hex(id(b_xy)))
            for x in range(0, n):
                if x == y:
                    b_xy = abs(A[x][y])
                else:
                    column_sum += abs(A[x][y])
                if column_sum > b_xy:
                    diagonaldominant = False
    return diagonaldominant

a=0
M1 = np.array([
    [2., 0., 0.],
    [1., 2., 0.],
    [0., 0., 3.],
])


M1_diag = ist_diagonaldominant(M1)
print(f"M1 = \n{M1}\n")
print(f"M1 diagonaldominant? -> {M1_diag}\n")
