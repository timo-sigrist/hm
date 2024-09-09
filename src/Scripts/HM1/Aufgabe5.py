from typing import Union
import enum
import numpy as np
import numpy.linalg

def calc_Norm1_Matrix(A):
    sum = np.sum(np.abs(A), axis=0)
    max = np.max(sum)
    return max


def calc_Norm1_Vektor(v):
    sum = np.sum(np.abs(v), axis=0)
    return sum

def jacobi(A: np.array, b: np.array, x0: np.array, tol: float) -> (np.array, Union[int, float], float, float):
    """Jacobi optimization.
    :param A: Matrix A
    :param b: Vector b
    :param x0: Vector x0 (estimation)
    :param tol: tolerance
    :return: List of [Iteration-Vector, n-Iterations, a-priori estimated steps]
    """
    print("\n#####  JACOBI  #####\n")
    L = np.tril(A, -1)
    print(f"L = \n{L}")
    D_inverted = np.diag(1 / np.diag(A))
    print(f"D^-1 = \n{D_inverted}")
    R = np.triu(A, 1)
    print(f"R = \n{R}")
    B = -np.matmul(D_inverted, (L + R))
    print(f"B = \n{B}\n")

    x_old = x0
    iterations = 0
    aposteriori = 0
    calc = True
    while calc:
        x_comp = np.matmul(np.matmul(-D_inverted, (L + R)), x_old) + np.matmul(D_inverted, b)
        aposteriori = calc_Norm1_Matrix(B) / (1 - calc_Norm1_Matrix(B)) * calc_Norm1_Vektor(x_comp - x_old)
        if (aposteriori < tol):
            calc = False
        x_old = x_comp
        iterations = iterations + 1

    return x_old, iterations, aposteriori


class Optimization(enum.Enum):
    JACOBI = (jacobi,)

    def __call__(self, *args, **kwargs):
        return self.value[0](*args, **kwargs)


def jacobi_gauss_seidel(A: np.array, b: np.array, x0: np.array, tol: float, opt: Optimization) -> (np.array, Union[int, float], float, float):
    """Optimize by either Jacobi or Gauss-Seidel.
    :param A: Matrix A
    :param b: Vector b
    :param x0: Vector x0 (estimation)
    :param tol: tolerance
    :param opt: optimization
    :return: List of [Iteration-Vector, n-Iterations, a-priori estimated steps]
    """
    return opt(A, b, x0, tol)


# Aufgabe 5b
A = np.array([[1, 0.3, 0, -0.3],
              [0.3, 1, -0.3, 0],
              [0, -0.3, 1, 0.3],
              [-0.3, 0, 0.3, 1]])

b = np.array([[2.3],
              [-1.3],
              [2.7],
              [-1.7]])

x0 = np.array([[-1],
               [-1],
               [1],
               [-1]])

aposterioriToleranz = 1e-3

(x, iterative, aposteriori) =  jacobi_gauss_seidel(A, b, x0, aposterioriToleranz, Optimization.JACOBI)
print(f"JACOBI: \n Iterative Lösung x = \n{x}\nIterationen = {iterative}\nAposteriori = {aposteriori}")

"""
Lösungen:
JACOBI: 
 Iterative Lösung x = 
[[ 1.99994922]
 [-1.00005078]
 [ 3.00005078]
 [-1.99994922]]
Iterationen = 18
Aposteriori = [0.00081248]
"""