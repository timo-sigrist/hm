import numpy as np


number_format = "{b:8.2f}"  # Formatierung der Zahl bei der Ausgabe von Matrizen


def QR_Zerlegung(A):
    A_copy = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A_copy = A_copy.astype('float64')  # change to float

    n = np.shape(A_copy)[0]

    if n != np.shape(A_copy)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A_copy

    n_iter = 1

    for j in np.arange(0, n - 1):
        a = np.copy(R[j:, j]).reshape(n - j, 1)
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = +1
        else:
            sig = -1
        v = a + sig * length_a * e
        u = (1 / np.linalg.norm(v)) * v
        H = np.eye(n - j) - 2 * np.dot(u, u.T)
        Qi = np.eye(n)
        Qi[j:, j:] = H
        R = np.dot(Qi, R)
        Q = np.dot(Q, Qi.T)

        print("Iteration:" + str(n_iter))
        print()
        print("### Q ###")
        print_extended_matrix(Q)
        print("### R ###")
        print_extended_matrix(R)
        n_iter = n_iter + 1

    return Q, R

def x_ausrechnen(Q, R, b):
    x = [0.0] * len(b)

    n = len(R)
    b_for_R = np.dot(Q.T, b)

    M = np.empty((n, n + 1), dtype=float)
    M[:, :n] = R
    M[:, n] = b_for_R

    for i in range(n - 1, -1, -1):
        # Rückwärtseinsetzen
        divider = M[i, i]
        vector = M[i, n]
        middlepart = vector

        for j in range(n)[1:n-i]:
            #print(middlepart)
            #print(M[i, n - j])
            #print(x[n - j])
            # zj - (bj / var aus M für bj) * zi
            middlepart = middlepart - M[i, n - j] * x[n - j]

        x[i] = middlepart / divider

    print(f"b: {b_for_R}")
    print(f"x: {x}")

    return

def print_extended_matrix(R):
    out = ""

    for row in range(R.shape[0]):
        lbracket = "|"
        rbracket = "|"

        if row == 0: lbracket = "/"; rbracket = "\\";
        if row == R.shape[0] - 1: lbracket = "\\"; rbracket = "/"
        if R.shape[0] == 1: lbracket = "("; rbracket = ")"

        out += lbracket
        out += " "

        for col in range(R.shape[1]):
            out += number_format.format(b=R[row, col])
            out += " "

        out += rbracket
        out += "\n"

    print(out)
