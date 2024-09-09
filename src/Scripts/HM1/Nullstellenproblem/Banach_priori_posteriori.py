import numpy as np


def F(x):
    return x ** 3 + 0.3


def F_ableitung(x):
    return 3 * x ** 2


def check_lipschitz_stetig_kontraktiv(Func, Func_deriv, a, b):
    F_x = Func(np.array([a, b]))
    F_min = np.min(F_x)
    F_max = np.max(F_x)
    F_ableitung_min = np.abs(Func_deriv(a))
    F_ableitung_max = np.abs(Func_deriv(b))
    F_lipschitz_const = max(F_ableitung_min, F_ableitung_max)
    print(f"\n\n|F_min - F_max| <= F_lipschitz_const * |a - b|")
    print(f"|{F_min}-{F_max}| <= {F_lipschitz_const} * |{a}-{b}|")
    print("Ausgerechnet:")
    print(f"{np.abs(F_min - F_max)} <= {F_lipschitz_const * np.abs(a - b)}")
    print(f"Lipschitz Constant: {F_lipschitz_const}")
    if abs(F_min - F_max) <= F_lipschitz_const * abs(a - b):
        print("Yes: Lipschitz stetig bzw. kontraktiv")
        print(f"-> F hat genau einen Fixpunkt approx NS in [{a}, {b}]")
        print(f"-> x_n+1=F(x_n) konvergiert gegen approx. NS für alle Startwerte x_0 in [{a}, {b}]")
    else:
        print("No: NOT Lipschitz stetig bzw. kontraktiv")
        print(f"-> F hat KEINEN Fixpunkt approx NS in [{a}, {b}]")
        print(f"-> x_n+1=F(x_n) konvergiert gegen approx. NS für alle Startwerte x_0 in [{a}, {b}]")
    return F_lipschitz_const


def fixpunkt_berechnen_apriori(funktion, x0, genauigkeit_e, alpha):
    # x0 = Startwert
    # x1 = Approximierter Nullpunkt
    # alpha = Lipschitzkonstante
    n = 0
    apriori = genauigkeit_e  # Obergrenze für a priori-Fehlerabschätzung
    x1 = funktion(x0)
    x0_original = x0
    x1_original = x1
    n = np.log(genauigkeit_e * (1 - alpha) / np.abs(x1 - x0)) / np.log(alpha)
    print("\n\nA priori:")
    print(f"Errechneter Fehler: {apriori}")
    print(f"Approx. Nullstelle: {x1}")
    print(f"Benötigte a priori-Iterationen: {n}")


def fixpunkt_berechnen_aposteriori(funktion, x0, genauigkeit_e, alpha):
    # x0 = Startwert
    # x1 = Approximierter Nullpunkt
    # alpha = Lipschitzkonstante
    n = 0
    aposteriori = genauigkeit_e
    x1 = funktion(x0)
    while not aposteriori < genauigkeit_e:
        aposteriori = alpha / (1 - alpha) * abs(x1 - x0)
        x0 = x1
        x1 = funktion(x0)
        n += 1
    print("\n\nA posteriori:")
    print(f"Errechneter Fehler: {aposteriori}")
    print(f"Approx. Nullstelle: {x1}")
    print(f"Benötigte a posteriori-Iterationen: {n}")


F_start = 0
F_end = 0.5
x0_fixpunkt = 0
genauigkeit = 10 ** -4

F_lipschitz_const = check_lipschitz_stetig_kontraktiv(F, F_ableitung, F_start, F_end)

fixpunkt_berechnen_apriori(F, x0_fixpunkt, genauigkeit, F_lipschitz_const)
fixpunkt_berechnen_aposteriori(F, x0_fixpunkt, genauigkeit, F_lipschitz_const)
