import numpy as np

from GaussAlgorithm import gauss
from GaussMitPivotisierung import gaussMitPivot

def printGaussResults(m,det,x):
     print("Obere Dreiecksmatrix:")
     print(m)
     print()
     print("Resultat-Vektor-X:")
     print(x)
     print()
     print("Determinante:")
     print(det)


A = np.array([
     (8,2),
     (2,8)
])
b = np.array([13.5,-22.5])

print("### Gauss ###")
m,det,x = gauss(A,b)
printGaussResults(m,det,x)

print("### Gauss Mit Pivot ###")
m,det,x = gaussMitPivot(A,b)
printGaussResults(m,det,x)
