basis = 2
mantisse = 52


def printNumber(number):
    print('{0:.30f}'.format(number))
    print(number)
def maschinengenauigkeitEigenerRechner():
    eps = 1
    while 1. + eps > 1:
        eps = eps/2
    printNumber(eps)
def maschinengenauigkeit(basis, mantisse):
    return (basis/2) * basis ** (-mantisse)

#Maschinengenauigkeit für parameter berechnen
eps = maschinengenauigkeit(basis, mantisse)
print("Maschinengenauigkeit:")
printNumber(eps)