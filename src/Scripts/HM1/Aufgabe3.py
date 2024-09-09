from sympy import Symbol
import sympy as sp
from sympy import diff
from sympy.core.expr import Expr
import numpy as np


class SecantMethod:
    def __init__(self, symbol: Symbol, function: Expr, x0: float, x1: float,
                 count: int = None, max_error: float = None) -> None:
        self.symbol = symbol
        self.func = function
        self.x0 = x0
        self.x1 = x1
        self.results = []
        self.max_error = max_error
        self.index = 0

        if count:
            for index in range(count):
                if index == 0:
                    self.append_secant(x0, x1)
                else:
                    self.append_secant(self.results[-1][1],
                                       self.results[-1][2])
        if max_error:
            self.run_until_max_error()

    def append_secant(self, x0: float, x1) -> None:
        next_value = x1 - ((x1 - x0) / (self.func.subs(self.symbol, x1) - self.func.subs(self.symbol, x0))) * self.func.subs(self.symbol, x1)
        self.results.append((x0, x1, next_value))

    def run_until_max_error(self):
        while True:
            if self.index == 0:
                self.append_secant(self.x0, self.x1)
            else:
                self.append_secant(self.results[-1][1], self.results[-1][2])
            self.index += 1
            if np.absolute(self.results[-1][1] - self.results[-1][2]) < self.max_error:
                self.results = self.results[:-1]
                self.index = self.index - 1
                break


class NewtonFehler:
    def __init__(self, symbol: Symbol, function: Expr, start_value: float,
                 error: float) -> None:
        self.symbol = symbol
        self.func = function
        self.start = start_value
        self.results = []
        self.append_newton(start_value)
        index = len(self.results)

        while np.abs(self.results[index-1][1] - self.results[index-1][0]) > error:
            self.append_newton(self.results[-1][1])
            index = len(self.results)

    def derivative(self) -> Expr:
        return diff(self.func, self.symbol)

    def append_newton(self, current_value: float) -> None:
        if not current_value:
            current_value = self.start
        next_value = (current_value - self.func.subs(self.symbol, current_value) / self.derivative().subs(self.symbol, current_value))
        self.results.append((current_value, next_value))


class Newton:
    def __init__(self, symbol: Symbol, function: Expr, start_value: float,
                 count: int) -> None:
        self.symbol = symbol
        self.func = function
        self.start = start_value
        self.results = []

        for index in range(count):
            if index == 0:
                self.append_newton(start_value)
            else:
                self.append_newton(self.results[-1][1])

    def derivative(self) -> Expr:
        return diff(self.func, self.symbol)

    def append_newton(self, current_value: float) -> None:
        if not current_value:
            current_value = self.start
        next_value = (current_value - self.func.subs(self.symbol, current_value) / self.derivative().subs(self.symbol, current_value))
        self.results.append((current_value, next_value))


#Aufgabe 3a
sym = Symbol("x")
function = (sp.exp(sym) + sp.exp(-sym))/(2 - sym -2)
x0 = 1.
x1 = 2.

secant = SecantMethod(sym, function, x0, x1, max_error=1e-7)
print("\n----- Secant Nullstelle: -----")
print(secant.results)
#Nullstelle: -2*(-E - exp(-1))/(-2*E - 2*exp(-1)) + 1)

#Aufgabe 3b
xStart = -1.0
newton = NewtonFehler(sym, function, xStart, 10**-7)
print("\n----- Newton negative Nullstelle: -----")
print(newton.results)