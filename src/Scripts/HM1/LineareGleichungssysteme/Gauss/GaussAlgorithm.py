import numpy as np

# solve A @ x = b
# A : a regular nxn matrix
# b : a n-dimensional vector

show_steps = True  # Ob die Zwischenresultate ausgegeben werden sollen
number_format = "{b:8.2f}"  # Formatierung der Zahl bei der Ausgabe von Matrizen

def gauss(A, b):
    n = np.shape(b)[0]
    M = np.empty((n, n + 1), dtype=float)
    M[:, :n] = A
    M[:, n] = b
    if show_steps:
        print_extended_matrix(M[:, :n], M[:, n])

    for i in range(n):
        # Koeffizienten eleminieren
        for j in range(i + 1, n):
            M[j, :] = M[j, :] - M[j, i] / M[i, i] * M[i, :]
            if show_steps:
                print_extended_matrix(M[:, :n], M[:, n])


    x = np.empty(n)

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

        # x[2] =  M[2, n]                                                           / M[2, n - 1]
        # x[1] = (M[1, n] -         M[1, n - 1] * x[2])                             / M[1, n - 2]
        # x[0] = (M[0, n] -         M[0, n-1] * x[2] - M[0, n - 2] * x[1])          / M[0, n - 3]

    det = np.prod(np.diagonal(M[:, :n]))

    return M[:, :n], det, x

def print_extended_matrix(R, v):
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

        out += "| "
        out += number_format.format(b=v[row])
        out += " "
        out += rbracket
        out += "\n"

    print(out)


