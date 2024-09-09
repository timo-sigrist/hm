import numpy as np
# Script S.90
# Von Mises Iteration / "Power Method" zum finden von
# Eigenvektoren/Eigenwerten:
# b_{k+1} = Ab_k / ||Ab_k||
#
# ! Findet den betragsmässig grössten Eigenwert (und Eigenvektor) !
#
A_matrix = np.array([
    [2., 0., 0.],
    [1., 2., 0.],
    [0., 0., 3.],
])

v_vektor = np.array(
    [1., 1., 1.]
)


n_iter = 0
max_iter = 10
λ = 0.0
abbruchbedingung = True

def calc_Norm2_Vektor(v):
    sum = np.sum(np.abs(v) ** 2, axis=0)
    return np.sqrt(sum)

while abbruchbedingung:
    w = A_matrix @ v_vektor
    print('w: ', w)
    v = w / np.linalg.norm(w)
    lambda_n = np.dot(v_vektor, w) / np.dot(v_vektor, v_vektor)
    n_iter += 1

    print()
    print('Iteration: ', n_iter)
    print('v: ', v)
    print('λ: ', lambda_n)

    if calc_Norm2_Vektor(v - v_vektor) < 10**-15:
        abbruchbedingung = False
    v_vektor = v
    λ = lambda_n

print()
print(f"Nach {n_iter} Iterationen")
print(f"Betragsmässig grösster Eigenwert: {λ}")
print(f"dazugehörender Eigenvektor: {v_vektor}\n")

eig_val, eig_vec = np.linalg.eig(A_matrix)
print("------------------------------------------------------------\n")
print(f"Check with np.linalg.eig():")
print(f"Eigenwert:\n{eig_val}")
print(f"Eigenvektor:\n{eig_vec}")
# für Eigenwert 3 & 1 -> (x - 3)(x - 1) = charakteristische Polynom lautet: p(x) = x^2 - 4x + 3 = (x - 3)(x - 1).

#Eigenräume
print("EigentRaum für Eigenwert "+str(eig_val[0])+" -> {x = a*(str("+str(eig_vec[0][0])+","+str(eig_vec[1][0])+","+str(eig_vec[2][0])+")^T; a in R}")
print("EigentRaum für Eigenwert "+str(eig_val[1])+" -> {x = a*(str("+str(eig_vec[0][1])+","+str(eig_vec[1][1])+","+str(eig_vec[2][1])+")^T; a in R}")
print("EigentRaum für Eigenwert "+str(eig_val[2])+" -> {x = a*(str("+str(eig_vec[0][2])+","+str(eig_vec[1][2])+","+str(eig_vec[2][2])+")^T; a in R}")