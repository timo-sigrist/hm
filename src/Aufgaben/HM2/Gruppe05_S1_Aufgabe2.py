import numpy as np
import matplotlib.pyplot as plt

def plot(x,y,z):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x,y,z)

    plt.title('Gitter')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

# b)
c = 1

def w(x,t):
    return np.sin(x + c*t)

def v(x,t):
    return np.sin(x + c*t) + np.cos(2*x + 2*c*t)

[x,y] = np.meshgrid(np.linspace(1, 10), np.linspace(1, 10))
z = w(x,y)
plot(x,y,z)

[x,y] = np.meshgrid(np.linspace(1, 10), np.linspace(1, 10))
z = v(x,y)
plot(x,y,z)
