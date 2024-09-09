import sympy as sp

if __name__ == '__main__':
    # Funktionen
    a, b, c = sp.symbols('a b c')
    f1 = a + b * sp.exp(c*1) - 40
    f2 = a + b * sp.exp(c*1.6) - 250
    f3 = a + b * sp.exp(c*2) - 800

    # Startvektor
    x1_start, x2_start, x3_start = 1,2,3

    print('Functions:')
    print(f1)
    print(f2)
    print(f3)
    print()

    # convert to matrix
    f = sp.Matrix([f1,f2,f3])
    print('Starting Matrix:')
    print(f)

    X = sp.Matrix([a,b,c])
    Df = f.jacobian(X)
    print('Jacobi Matrix:')
    print(Df)

    # Werte einsetzen
    print()
    print('values of jacobian matrix:')
    Df0 = Df.subs([(a,x1_start),(b,x2_start),(c,x3_start)])
    print(Df0)
    print(Df0.evalf())
