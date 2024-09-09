import numpy as np

from Gruppe05_S8_Aufgabe1 import *

def f(x):
    return m/(-x * np.sqrt(x))

# derivative of f(x)
def df(x):
    return 2 * m * 1/np.sqrt(x)

if __name__ == '__main__':
    print("starting...")
    n = 5
    m = 10
    b = 5  # v
    a = 20  # v0

    via_rechteck = SumRf(f, a, b, n)
    via_trapez = SumTf(f, a, b, n)
    via_simpson = SumSf(f, a, b, n)

    exact = np.abs(df(b)-df(a))

    print("Exercise 2: ")
    print(f"a) with rechteck = {via_rechteck}\twith absolute error: {np.abs(exact-via_rechteck)}")
    print(f"b) with trapez = {via_trapez}\twith absolute error: {np.abs(exact-via_trapez)}")
    print(f"c) with simpson = {via_simpson}\twith absolute error: {np.abs(exact-via_simpson)}")
    print(f"exact = {exact}")
