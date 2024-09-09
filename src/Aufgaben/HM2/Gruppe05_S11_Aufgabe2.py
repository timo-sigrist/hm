import numpy as np
from Eulerverfahren import euler, mittelpunkt, modEuler

if __name__ == "__main__":
    f = lambda x, y: x ** 2 / y
    a = 0
    b = 2.1
    y0 = 2
    h = 0.7
    n = int((b - a) / h)

    resultEuler = euler(f, a, b, n, y0)
    print("Euler klassisch")
    print(resultEuler)

    resultMittelpunkt = mittelpunkt(f, a, b, n, y0)
    print("Mittelpunkt")
    print(resultMittelpunkt)

    resultModifizeirt = modEuler(f, a, b, n, y0)
    print("Euler modifiziert")
    print(resultModifizeirt)

    yexakt = lambda x: np.sqrt(2 * x ** 3 / 3 + 4)

    eulererr = abs(resultEuler[1] - yexakt(resultEuler[0]))
    mittelpunkterr = abs(resultMittelpunkt[1] - yexakt(resultMittelpunkt[0]))
    modeulererr = abs(resultModifizeirt[1] - yexakt(resultModifizeirt[0]))

    print("-------------------------------------------------")
    print('Absolute Fehler für die folgenden Verfahren:')
    print('Euler-Verfahren: ', eulererr)
    print('Modifiziertes Euler-Verfahren: ', modeulererr)
    print('Mittelpunkt-Verfahren: ', mittelpunkterr)
