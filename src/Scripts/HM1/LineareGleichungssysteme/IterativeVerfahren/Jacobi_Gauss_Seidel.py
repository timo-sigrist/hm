from typing import Union
import enum
import numpy as np
import numpy.linalg


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
        aposteriori = np.linalg.norm(B, np.inf) / (1 - np.linalg.norm(B, np.inf)) * np.linalg.norm((x_comp - x_old), np.inf)
        if (aposteriori < tol):
            calc = False
        x_old = x_comp
        iterations = iterations + 1

    apriori = np.ceil(np.log((tol * (1 - np.linalg.norm(B, np.inf))) / (
        np.linalg.norm((np.matmul(np.matmul(-D_inverted, (L + R)), x0) + np.matmul(D_inverted, b) - x0), np.inf)
    )) / np.log(np.linalg.norm(B, np.inf)))

    return x_old, iterations, apriori, aposteriori


def seidel(A: np.array, b: np.array, x0: np.array, tol: float) -> (np.array, Union[int, float], float):
    """Gauss Seidel optimization.
    :param A: Matrix A
    :param b: Vector b
    :param x0: Vector x0 (estimation)
    :param tol: tolerance
    :return: List of [Iteration-Vector, n-Iterations, a-priori estimated steps]
    """

    print("\n #####  SEIDEL  #####\n")
    L = np.tril(A, -1)
    print(f"L = \n{L}")
    D = np.diag(np.diag(A))
    print(f"D = \n{D}")
    R = np.triu(A, 1)
    print(f"R = \n{R}")
    B = -np.matmul(-np.linalg.inv(D + L), R)
    print(f"B = \n{B}\n")

    x_old = x0
    iterations = 0
    calc = True
    while calc:
        x_comp = np.matmul(np.matmul(-np.linalg.inv(D + L), R),x_old) + np.matmul(np.linalg.inv(D + L), b)
        aposteriori = np.linalg.norm(B, np.inf) / (1 - np.linalg.norm(B, np.inf)) * np.linalg.norm((x_comp - x_old), np.inf)
        if (aposteriori < tol):
            calc = False
        x_old = x_comp
        iterations = iterations + 1

    apriori = np.ceil((
        np.log((tol * (1 - np.linalg.norm(B, np.inf))) /
        (np.linalg.norm((np.matmul(np.matmul(-np.linalg.inv(D + L), R), x_old) + np.matmul(np.linalg.inv(D + L), b) - x0), np.inf)))
        ) / np.log(np.linalg.norm(B, np.inf))
    )
    return x_old, iterations, apriori


class Optimization(enum.Enum):
    JACOBI = (jacobi,)
    SEIDEL = (seidel,)

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


# Bei Fehler Matrix maneull pivotisieren (höchste zahl auf A11 setzen) und b Vektor auch anpassen!!!
A = np.array([[4, -1, 1],
              [-2, 5, 1],
              [1, -2, 5]])

b = np.array([[5],
              [11],
              [12]])

x0 = np.array([[0],
               [0],
               [0]])

tolerance = 1e-4

if __name__ == '__main__':
    (x, iterative, apriori, aposteriori) =  jacobi_gauss_seidel(A, b, x0, tolerance, Optimization.JACOBI)
    print(f"JACOBI: \n Iterative Lösung x = \n{x}\nIterationen = {iterative}\nApriori = {apriori}\nAposteriori = {aposteriori}")
    (x, iterative, apriori) = jacobi_gauss_seidel(A, b, x0, tolerance, Optimization.SEIDEL)
    print(f"SEIDEL: \n Exakte Lösung x = \n{x}\nIterationen = {iterative}\nApriori = {apriori}")
