import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return x**3 + 0.3


def F_ableitung(x):
    return 3*x**2

def checkIfXisAbstossendOrAnziehend(fixpunkt):
    if (np.absolute(F_ableitung(fixpunkt)) < 1):
        return "Der Fixpunkt " + str(fixpunkt) + " ist anziehend."
    else:
        return "Der Fixpunkt " + str(fixpunkt) + " ist abstossend."


def calculateValues(x0, intervallstart, intervallend, intervalljumps):
    xvalues.append(x0)

    xn = x0
    for n in np.arange(intervallstart, intervallend, intervalljumps):
        xn_plus_one = F(xn)

        xvalues.append(xn_plus_one)

        print("\n########### \n Iteration: " + str(n) + "\n x gleich: " + str(xn) + "\n nächstes x: " + str(xn_plus_one) + "\n""###########")
        xn = xn_plus_one

    fixpunkt = xn_plus_one
    return fixpunkt


xvalues = []
x0 = -1
intervallstart = 0
intervallend = 10
intervalljumps = 1

fixpunkt = calculateValues(x0, intervallstart, intervallend, intervalljumps)
print("\n########### \n Tabelle \n " + str(xvalues) + "\n########### \n")
print("\n########### \n Fixpunkt \n " + str(fixpunkt) + "\n " + str(checkIfXisAbstossendOrAnziehend(fixpunkt)) + "\n########### \n")

plt.plot(xvalues, label="F(x)")
plt.grid()
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Fixpunktiteration F(x) = x")
plt.legend()
plt.show()
