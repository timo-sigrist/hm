import sympy as sp
import numpy as np

# a, b, c, d, e, f, g, h, i, j, k, l = sp.symbols('a b c d e f g h i j k l')
# m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('m n o p q r s t u v w x y z')
# x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = sp.symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_all_used_symbols(vector):
    """
    Takes an input vector, analyses all functions contained in it and returns all
    variables in a sorted array

    Parameters:

    vector: Function-vector, containing multiple functions

    Returns:

    symbols: all used variables in a sorted array

    """

    if hasattr(vector, '__iter__') is False:
        vector = sp.Matrix([vector])

    atoms = []
    for function in vector:
        variables = function.atoms(sp.Symbol)
        for variable in variables:
            if str(variable) not in atoms:
                atoms.append(str(variable))

    atoms.sort()
    symbols = []

    for atom in atoms:
        for function in vector:
            for variable in function.atoms(sp.Symbol):
                if str(variable) == atom and variable not in symbols:
                    symbols.append(variable)

    return symbols


def list_to_ndarray(list):
    ndarray = np.copy(list[0])

    for i, v in enumerate(list[1:]):
        ndarray = np.append(ndarray, v, axis=1)

    return ndarray


def error(*args, sep=' ', end='\n', file=None):
    for val in args:
        print(f"{bcolors.FAIL}{val}{bcolors.ENDC}", sep, end, file)
