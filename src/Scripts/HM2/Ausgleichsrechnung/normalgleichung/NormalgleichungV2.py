import numpy as np
import matplotlib.pyplot as plt

def f0(x): #c
    x_dum = np.copy(x)
    x_dum[:] = 1
    return x_dum

def f1(x) : #T
    x_dum = np.copy(x)
    x_dum[:] = x_dum
    return x_dum[:]

def f2(x) : #T^2
    x_dum = np.copy(x)
    x_dum[:] = x_dum**2
    return x_dum[:]

def f3(x) :#T^3
    x_dum = np.copy(x)
    return x_dum**3

def f4(x) :#T^4
    x_dum = np.copy(x)
    x_dum[:] = x_dum**4
    return x_dum[:]

def f(x, lam):
    # Ausgleichsrechnung aT^3 + bT^2 + bT + c
    return lam[0]*f0(x) + lam[1]*f1(x) + lam[2]*f2(x) + lam[3]*f3(x) + lam[4]*f4(x)


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5]
    y = [0.54, 0.44, 0.28, 0.18, 0.12, 0.08]

    A = np.zeros((len(x), 5)) # 5 Spalten
    A[:,0] = f0(x)
    A[:,1] = f1(x)
    A[:,2] = f2(x)
    A[:,3] = f3(x)
    A[:,4] = f4(x)
    print(A)

    #ohne QR Zerlegung
    lam = np.linalg.solve(A.T@A, A.T@y)

    #mit QR Zerlegung
    [Q,R] = np.linalg.qr(A)
    lam_qr = np.linalg.solve(R,Q.T.dot(y))

    print("Lamda:", lam)

    x_fine=np.arange(x[0],x[-1],0.1)
    plt.plot(x_fine,f(x_fine,lam), color = '#00FF00')
    #plt.plot(x_fine,f(x_fine,lam_qr), color = '#red')
    plt.legend(["normal"])
    plt.plot(x,y,'o', color = '#FF0000')
    plt.show()