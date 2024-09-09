# Numerische Integration

# RechteckRegel
def Rf(_func, _a, _b):
    return _func((_a + _b) / 2) * (_b - _a)


# Summierte RechteckRegel
def SumRf(_func, _a, _b, _n):
    sum = 0.
    h = (_b - _a) / _n
    # we don't do _n-1 because range() already stops at n-1
    for i in range(0, _n):
        x = _a + i*h
        sum += _func(x + h/2)
    return h * sum


# TrapezRegel
def Tf(_func, _a, _b):
    return (_func(_a) + _func(_b)) / 2 * (_b - _a)


# Summierte TrapezRegel
def SumTf(_func, _a, _b, _n):
    sum = 0.
    h = (_b - _a) / _n
    # we don't do _n-1 because range() already stops at n-1
    for i in range(1, _n):
        x = _a + i*h
        sum += _func(x)
    return h * ((_func(_a) + _func(_b) / 2) + sum)


def SumSf(_func, _a, _b, _n):
    sumTf = 0.
    sumRf = 0.
    h = (_b - _a) / _n
    # sumTf
    for i in range(1, _n):
        x = _a + i*h
        sumTf += _func(x)
    # sumRf
    for i in range(1, _n+1):
        x = _a + i*h
        x_minus_one = _a + (i-1)*h
        sumRf += _func((x_minus_one + x) / 2)

    return h/3 * (1/2 * _func(_a) + sumTf + 2*sumRf + 1/2 * _func(_b))


def Sf(_func, _a, _b):
    return 1/3 * (Tf(_func, _a, _b)+2*Rf(_func, _a, _b))



def f(x):
    return 1/x


if __name__ == '__main__':
    a = 2
    b = 4

    rf = Rf(f, a, b)
    print('rf: ' + str(rf))

    tf = Tf(f, a, b)
    print('tf: ' + str(tf))

    sumRf = SumRf(f, a, b, 4)
    print('sumRf: ' + str(sumRf))

    sumTf = SumTf(f, a, b, 4)
    print('sumTf: ' + str(sumTf))

    sumSf = SumSf(f, a, b, 4)
    print('sf: ' + str(sumSf))
