import numpy as np

# solve A @ x = b with pivotisierung
# A : a regular nxn matrix
# b : a n-dimensional vector

show_steps = True  # Ob die Zwischenresultate ausgegeben werden sollen
number_format = "{b:8.2f}"  # Formatierung der Zahl bei der Ausgabe von Matrizen


def gaussMitPivot(A, b):
    n = np.shape(b)[0]
    M = np.empty((n, n + 1), dtype=float)
    M[:, :n] = A
    M[:, n] = b
    if show_steps:
        print_extended_matrix(M[:, :n], M[:, n])

    for i in range(n):
        # Zeilen tauschen (evtl, mit Pivotisierung)
        A_copy = np.copy(M[:, :n])
        b_copy = np.copy(M[:, n])
        switch_rows_for_column_pivoting(A_copy, b_copy, i)
        M[:, :n] = A_copy
        M[:, n] = b_copy

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


def switch_rows_for_column_pivoting(A_copy, b_copy, i):
    row_inversion_count = 0

    pivot = 0
    pivot_row = 0

    for row in np.arange(i, A_copy.shape[0], 1):
        if abs(A_copy[row, i]) > pivot:
            pivot = abs(A_copy[row, i])
            pivot_row = row

    if pivot == 0:
        raise Exception('All elements in first column are zero. System has no single solution.')

    if 0 < pivot_row != i:
        # Switch pivot row with first row
        r_copy = np.copy(A_copy)
        A_copy[i, :] = r_copy[pivot_row, :]
        A_copy[pivot_row, :] = r_copy[i, :]

        v_copy = np.copy(b_copy)
        b_copy[i] = v_copy[pivot_row]
        b_copy[pivot_row] = v_copy[i]

        row_inversion_count += 1
        if show_steps:
            print("|Pivot| ist " + str(pivot) + " --> Vertausche Zeile " + str(i + 1) + "  mit Zeile " + str(pivot_row + 1) + ".")
            print_extended_matrix(A_copy, b_copy)

    else:
        if show_steps:
            print("Keine Zeilenvertauschungen notwendig!")

    return row_inversion_count


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
