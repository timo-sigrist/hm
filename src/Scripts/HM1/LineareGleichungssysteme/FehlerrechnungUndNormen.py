import numpy as np
print()

vektorenNorm = False
matrixNorm = False
absrelKond = True

def calc_Norm1_Matrix(A):
    sum = np.sum(np.abs(A), axis=0)
    max = np.max(sum)
    return max


def calc_NormInf_Matrix(A):
    sum = np.sum(np.abs(A), axis=1)
    max = np.max(sum)
    return max

if matrixNorm:
    A = np.array([
        [4.0, -1, 0, 0, 0, 0],
        [-1, 4.0, -1, 0, 0, 0],
        [0, -1, 4.0, -1, 0, 0],
        [0, 0, -1, 4.0, -1, 0],
        [0, 0, 0, -1, 4.0, -1],
        [0, 0, 0, 0, -1, 4.0]
    ])

    A_norm1 = calc_Norm1_Matrix(A)
    print(f"1. Norm: {A_norm1}")

    A_normInf = calc_NormInf_Matrix(A)
    print(f"Inf. Norm: {A_normInf}")

print()
# -------------------------------------------------- Vektor
print()

def calc_Norm1_Vektor(v):
    sum = np.sum(np.abs(v), axis=0)
    return sum


def calc_Norm2_Vektor(v):
    sum = np.sum(np.abs(v) ** 2, axis=0)
    return np.sqrt(sum)


def calc_NormInf_Vektor(v):
    max = np.max(np.abs(v))
    return max


if vektorenNorm:
    v = np.array([-1, 2, 3])

    v_norm1 = calc_Norm1_Vektor(v)
    print(f"1. Norm: {v_norm1}")

    v_norm2 = calc_Norm2_Vektor(v)
    print(f"1. Norm: {v_norm2}")

    v_normInf = calc_NormInf_Vektor(v)
    print(f"Inf. Norm: {v_normInf}")

# ------------ Absoulter / Relativer Fehler / Konditionszahl

def konditionszahl(A):
    cond = calc_NormInf_Matrix(A) * calc_NormInf_Matrix(np.linalg.inv(A))
    return cond

def absoluterFehler(A, b, bFehlertoleranz):
    absFehler = calc_NormInf_Matrix(np.linalg.inv(A)) * calc_NormInf_Vektor(b - b * (1+bFehlertoleranz))
    return absFehler

def relativerFehler(A, b, bFehlertoleranz):
    relFehler = konditionszahl(A) * (calc_NormInf_Vektor(b - b * (1+bFehlertoleranz)) / calc_NormInf_Vektor(b))
    return  relFehler

def relativerFehlerAGestoert(A , AMaxStoerProElement, b, bFehlertoleranz):
    aAbsoluterFehler = AMaxStoerProElement * len(A)
    aRelativerFehler = aAbsoluterFehler / calc_NormInf_Matrix(A)
    condA = konditionszahl(A)
    if  condA *  aRelativerFehler < 1:
        xRelativerFehler = (condA / (1 - condA * aRelativerFehler)) * (aRelativerFehler + (calc_NormInf_Vektor(b - b * (1 + bFehlertoleranz)) / calc_NormInf_Vektor(b)))
    else:
        raise Exception("Bedingung cond(A) * absoluter Fehler A < 1")
    return  xRelativerFehler

if absrelKond:
    A = np.array([(2,4),(4,8.1)])
    b = np.array([1,1.5])
    bMaxFehlertoleranz = 0.1 # der Maximale Fehler der zwischen b und b gestört passieren kann/ist
    aMaxFehlertoleranz = 0.003

    condA = konditionszahl(A)
    absFehler = absoluterFehler(A, bMaxFehlertoleranz)
    relFehler = relativerFehler(A, b, bMaxFehlertoleranz)
    relFehlerMitAGest = relativerFehlerAGestoert(A, aMaxFehlertoleranz, b, bMaxFehlertoleranz)

    print("### Konditionszahl ###")
    print(condA)
    print("### Absoulter Fehler ###")
    print(absFehler)
    print("### Relativer Fehler ###")
    print(relFehler)
    print("### Relativer Fehler mit A gestört")
    print(relFehlerMitAGest)
