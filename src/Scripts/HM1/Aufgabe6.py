import numpy as np

# Aufgabe 6b

def calc_Norm2_Vektor(v):
    sum = np.sum(np.abs(v) ** 2, axis=0)
    return np.sqrt(sum)

A_matrix = np.array([
    [3., 0., 0.],
    [1., 3., 2.],
    [0., 0., 6.],
])

v_vektor = np.array(
    [1., 1., 1.]
)

toleraz = 10**-15
λ = 0.0

vold = np.array(
    [0., 0., 0.]
)
while calc_Norm2_Vektor(v_vektor - vold) > toleraz:
    vold = v_vektor
    w = A_matrix @ v_vektor
    v = w / np.linalg.norm(w)
    lambda_n = np.dot(v_vektor, w) / np.dot(v_vektor, v_vektor)

    print()
    print('v: ', v)
    print('λ: ', lambda_n)

    v_vektor = v
    λ = lambda_n

print()
print(f"Betragsmässig grösster Eigenwert: {λ}")
print(f"dazugehörender Eigenvektor: {v_vektor}\n")

eig_val, eig_vec = np.linalg.eig(A_matrix)
print("------------------------------------------------------------\n")
print(f"Check with np.linalg.eig():")
print(f"Eigenwert:\n{eig_val}")
print(f"Eigenvektor:\n{eig_vec}")
# für Eigenwert 3 & 1 -> (x - 3)(x - 1) = charakteristische Polynom lautet: p(x) = x^2 - 4x + 3 = (x - 3)(x - 1).

#Eigenräume
print("EigentRaum für Eigenwert "+str(eig_val[0])+" -> {x = a*("+str(eig_vec[0][0])+","+str(eig_vec[1][0])+","+str(eig_vec[2][0])+")^T; a in R}")
print("EigentRaum für Eigenwert "+str(eig_val[1])+" -> {x = a*("+str(eig_vec[0][1])+","+str(eig_vec[1][1])+","+str(eig_vec[2][1])+")^T; a in R}")
print("EigentRaum für Eigenwert "+str(eig_val[2])+" -> {x = a*("+str(eig_vec[0][2])+","+str(eig_vec[1][2])+","+str(eig_vec[2][2])+")^T; a in R}")