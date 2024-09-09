import numpy as np


def eigenvec(A, eigenwert):
    n = np.shape(A)[0]
    eigengleichung = A - eigenwert * np.eye(n)
    print(eigengleichung)
    return np.linalg.solve(eigengleichung, np.array([0, 0, 0]))


number_format = "{b:8.2f}"  # Formatierung der Zahl bei der Ausgabe von Matrizen
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

A_matrix = np.array([
    [1, -2, 0],
    [2, 0, 1],
    [0, -2, 1],
], dtype=float)

A_dim = np.shape(A_matrix)[0]
P_i = np.eye(A_dim)
A_i = np.copy(A_matrix)
n_iter = 100

for i in range(0, n_iter):
    Q_i, R_i = np.linalg.qr(A_i)
    A_i = Q_i @ R_i
    A_i = R_i @ Q_i
    P_i = P_i @ Q_i

print(f"Matrix A_i nach {n_iter} Iterationen:\n{A_i}\n")
print("clean print:")
print_extended_matrix(A_i)


# Wenn obere dreiecksmatrix
if np.allclose(A_i, np.triu(A_i)):
    print("A_i ist eine obere Dreiecksmatrix => Eigenwerte direkt ablesbar (\"perfekte\" obere Dreiecksmatrix).")
    print("Eigenwerte:")
    eigenwerte = np.diag(A_i)
    for i in range(0, len(eigenwerte)):
        print(f" λ{i + 1} = {eigenwerte[i]}")
    # print("Eigenvektoren:")
    # for i in range(0, len(eigenwerte)):
    # eigvec = eigenvec(A_i.round(), round(eigenwerte[i], 1))
    # print(f" x{i+1} = {eigvec}")
else:
    print("A_i ist keine reine obere Dreiecksmatrix, d.h. es treten 2x2 Blöcke auf")
    print("Gewisse untere Dreieckselemente verschwinden nicht, egal wie viele Iterationen.")
    print("ToDo: Manuell 2x2 Blöcke finden. Wie Kap.4 Teil2 Slide 113 vorgehen.")
    print(f"p(λ) = ({A_i[0,0]}-λ)({A_i[1,1]}-λ) - ({A_i[0,1]})({A_i[1,0]})")
