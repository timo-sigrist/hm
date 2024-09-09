from sympy import Symbol
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
