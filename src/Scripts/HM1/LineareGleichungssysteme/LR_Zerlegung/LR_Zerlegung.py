import numpy as np

# Angegebene Matrixspalte untersuchen, um nächstbests Pivot-Element (ungleich 0) zurückzugeben.
def pivot_suchen(A, i):
    print("Suche Pivotelement...")

    pivot = 0
    pivot_row = 0

    for row in np.arange(i, A.shape[0], 1):
        if abs(A[row, i]) > pivot:
            pivot = abs(A[row, i])
            pivot_row = row

    if pivot == 0:
        raise Exception('All elements in first column are zero. System has no single solution.')
    else:
        print(f"Pivot gefunden in Zeile {pivot_row+1}: A_{pivot_row}_{i} = {A[pivot_row][i]}")

    return pivot_row

# Zeilen tauschen
def swap(matrix, von, zu):
    if von == zu:
        return
    matrix_copy = np.copy(matrix)
    matrix[von, :] = matrix_copy[zu, :]
    matrix[zu, :] = matrix_copy[von, :]
    print(f"SWAP: Tausche Zeile {von+1} mit Zeile {zu+1}\n")

def LR_zerlegung_PLR(Matrix):
    A = np.array(Matrix, dtype=float) # A-Matrix kopieren
    n = len(A) # Anzahl Zeilen bestimmen
    L = np.eye(n) # Einheitsmatrix erstellen für L
    R = np.copy(A)
    P = np.eye(n) # Permutationsmatrix vorbereiten mittels Erstellung einer Einheitsmatrix
    for zeile in range(n - 1):
        print(f"\nZwischenschritt: {zeile + 1}")
        print(f"L:\n{L}\n")
        print(f"R:\n{R}\n")
        print(f"P:\n{P}\n")

        for rest_zeile in range(zeile + 1, n):
            eliminations_faktor = R[rest_zeile][zeile] / R[zeile][zeile]
            print(f"Eliminationsfaktor Zeile {rest_zeile}: {R[rest_zeile][zeile]} / {R[zeile][zeile]}")
            L[rest_zeile][zeile] = eliminations_faktor
            for spalte in range(zeile, n):
                R[rest_zeile][spalte] = R[rest_zeile][spalte] - eliminations_faktor * R[zeile][spalte]

    return P, L, R

def y_ausrechnen(L, b):
    y = [0.0] * len(b)
    for zeile in range(len(L)):
        summe = 0
        for spalte in range(0, zeile):
            summe += y[spalte] * L[zeile][spalte]
        y[zeile] = (b[zeile] - summe) / L[zeile][zeile]
    return y


def x_ausrechnen(P, L, R, b_original):
    b = P @ b_original
    y = y_ausrechnen(L, b)
    x = [0.0] * len(b)

    print(f"y: {y}")
    print(f"L: {L}")
    print(f"b: {b}")

    for zeile in reversed(list(range(0, len(R)))):
        summe = 0
        for spalte in range(zeile, len(R[zeile])):
            summe += x[spalte] * R[zeile][spalte]
        x[zeile] = (y[zeile] - summe) / R[zeile][zeile]

    print(f"x: {x}")

    return x

def lrZerlegung(A,b):
    print("LR-Zerlegung mit Permutationsmatrix:\n")
    P, L, R = LR_zerlegung_PLR(A)
    x = x_ausrechnen(P, L, R, b)

    print("\nResultat:")
    print(f"L:\n{L}\n")
    print(f"R:\n{R}\n")
    print(f"P:\n{P}\n")

    return L,R,x,P
