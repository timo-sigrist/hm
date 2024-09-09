# Aufgabenstellung Skript
# Wie viele verschiedene Maschinenzahlen gibt es auf einem Rechner, der
# 20-stellige Gleitpunktzahlen mit 4-stelligen binären Exponenten sowie dazugehörige Vorzeichen im Dualsystem verwendet? Wie lautet die kleinste
# positive und die größte Maschinenzahl?

# Alle Stellen nach dem Punkt bsp. 0.12345678 = 8
mantisse = 15
# bsp. binary
basis = 2
# soll das Vorzeichen mitgerechnet werden?
vorzeichen = True
# Stellen des Exponenten
exponenten = 5
# Bei exponenten = 4 -> 1111 -> 15
emax = 15
# emin bei nur positiven Zahlen -> 0
emin = -15


def xmax(basis, emax, mantisse):
    return (1 - basis ** -mantisse) * (basis ** emax)


def xmin(basis, emin):
    return basis ** (emin - 1)


def max_maschinenzahl(basis, mantisse, exponenten, vorzeichen):
    if vorzeichen:
        # Da die Null doppelt gezählt wurde rechnen wir noch -1
        return (basis ** (mantisse+1)) * ((basis ** (exponenten + 1)) - 1)
        # Würde man die Null nicht beachten gäbe es:
        # return (basis ** (mantisse+1)) * (basis ** (exponenten + 1))
    else:
        return (basis ** mantisse) * (basis ** exponenten)



# normierte Maschinenzahlen von Hand berechnen falls benötigt
# punkt nach rechts: hoch minus
x_max = xmax(basis, emax, mantisse)
x_min = xmin(basis, emin)

print("##### X Max #####")
print(x_max)
print("##### X Min #####")
print(x_min)

# Anzahl verschiedene Maschinenzahlen
# Manitsse -1, weil die erste Nachkommaziffer muss 1 sein
max_Anzahl_diff_Maschinenzahlen = max_maschinenzahl(basis, mantisse-1, exponenten, vorzeichen)

print("##### Anzahl verschiedene Maschinenzahlen #####")
print(str(max_Anzahl_diff_Maschinenzahlen))
print("plus 1 für die Zahl 0")
print(str(max_Anzahl_diff_Maschinenzahlen + 1))
