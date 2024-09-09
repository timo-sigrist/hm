import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot(x,y,z):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x,y,z)

    plt.title('Gitter')
    ax.set_xlabel('Geschwindigkeit')
    ax.set_ylabel('Winkel')
    ax.set_zlabel('Distanz')

    plt.show()


    # %matplotlib notebook
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,z)

    plt.title('Fläche')
    ax.set_xlabel('Geschwindigkeit')
    ax.set_ylabel('Winkel')
    ax.set_zlabel('Distanz')

    plt.show()


    fig = plt.figure(3)
    ax = fig.add_subplot(111)

    cont = plt.contour(x, y, z, cmap=cm.coolwarm)
    fig.colorbar(cont, shrink=0.5, aspect=5)

    plt.title('Höhenlinien')
    ax.set_xlabel('Geschwindigkeit')
    ax.set_ylabel('Winkel')

    plt.show()

# a)
def W(v0, alpha):
    g = 9.81
    return (v0**2 * np.sin(2*alpha)) / g

v = np.arange(0, 100, 0.01)
alpha = np.arange(0, np.pi/2, 0.01)

[x,y] = np.meshgrid(v, alpha)
z = W(x,y)

plot(x,y,z)


# Bei welchem Winkel α erreicht W für gegebens v0 sein Maximum?
# aphla = 0.8

# b)

# Gaskonstante
R = 8.31
def p(V, T):
    return R*T/V

def V(p, T):
    return R*T/p

def T(p,V):
    return p*V/R

v = np.linspace(0.001, 0.2)
t = np.linspace(0.001, 1e4)
[x,y] = np.meshgrid(v, t)
z = p(x,y)

plot(x,y,z)

p = np.linspace(1e4, 1e5)
t = np.linspace(0.001, 1e4)
[x,y] = np.meshgrid(p, t)
z = V(x,y)

plot(x,y,z)

p = np.linspace(1e4, 1e6)
v = np.linspace(0.001, 10)
[x,y] = np.meshgrid(p, v)
z = T(x,y)

plot(x,y,z)