import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return (48*x**2 -12)/-16


def F_ableitung(x):
    return -6*x


basis = 10
mantisse = 3
exponent = 3

# xExakt = 180.1234567 -> normalisieren zu 0.1801234567 * 10 ** 3
# xExakt ohne Exponent -> wird unten dazugerechnet
xExakt = 1.46


def printNumber(number):
    print('{0:.30f}'.format(number))
    print(number)


def absoulterFehler(xExakt, mantisse, basis, exponent):
    rounded = round(xExakt, mantisse)
    print("gerundete Nummer: " + str(rounded) + " * " + str(basis) + "^" + str(exponent))
    return np.abs(rounded - xExakt) * basis ** exponent

def relativerFehler(absFehler, xExakt):
    return absFehler/np.abs(xExakt)

absFehler = absoulterFehler(xExakt, mantisse, basis, exponent)
relFehler = relativerFehler(absFehler, xExakt*basis**exponent)

print("Absoulter Fehler:")
printNumber(absFehler)
print("Relativer Fehler:")
printNumber(relFehler)
