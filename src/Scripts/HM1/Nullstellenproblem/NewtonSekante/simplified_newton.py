from sympy import Symbol
from sympy import diff
from sympy.core.expr import Expr


class SimplifiedNewton:
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
        next_value = (current_value - self.func.subs(self.symbol, current_value) / self.derivative().subs(self.symbol, self.start))
        self.results.append((current_value, next_value))
