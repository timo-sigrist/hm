from sympy import Symbol
from sympy import diff
from sympy.core.expr import Expr
import numpy as np


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
