import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x/np.log(x)


def f_ableitung(x):
    return (np.log(x)-1)/(np.log(x))**2


def K(x):
    return (np.absolute(f_ableitung(x) * np.absolute(x))) / (np.absolute(f(x)))

# Aufgabe 2a
print("Näherungsweise relativer Fehler")
x0 = 3
absoluterFehlerX = 0.1
konditionszahl = K(x0)
absoluterFehlerFunc = np.abs(f_ableitung(x0)) * absoluterFehlerX
relativerFehlerFunc = konditionszahl * (absoluterFehlerX/np.abs(x0))
print("Relativer Fehler f(x0): " + str(relativerFehlerFunc))

#Aufgabe 2b
x = np.arange(0, 10, 0.1)

plt.semilogy(x,K(x))
plt.show()
print("Alle Konditionszahlen: \n" + str(K(x)))

# nr_fuer_gut_konditioniert = 1
xkleiner = []
xgroesser = []
for x_wert in x:
    if K(x_wert) <= 1.:
        xkleiner.append(x_wert)
    if K(x_wert) > 1:
        xgroesser.append(x_wert)

print(xkleiner)
print("------------")
print(xgroesser)
#b ist die Zahl die in xkleiner und xgrösser vorhanden ist

