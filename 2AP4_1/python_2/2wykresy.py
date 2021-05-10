import numpy as np
import matplotlib.pyplot as plt

def f1():
    # return np.exp(-t) * np.cos(2 * np.pi * t)
    lx = np.arange(0.0, 5.0, 0.1)
    ly = [np.exp(-y) * np.cos(2 * np.pi * y) for y in lx]
    plt.grid()
    plt.title("Funkcja 1")
    plt.plot(lx, ly, 'k')


def f2():
    lx = np.arange(0.0, 5.0, 0.02)
    ly = [np.cos(2 * np.pi * y) for y in lx]
    plt.legend("f(cos(x))")
    plt.plot(lx, ly, 'r--')


def f3():
    lx = list(range(-10, 11))
    a, b, c = 1, -3, 1
    ly = [a * (x**2) + b * x + c for x in lx]
    plt.plot(lx, ly, 'go')


def main():
    plt.figure(1)
    fig = plt.gcf()
    fig.set_size_inches(8, 8)
    
    plt.subplot(221)
    f1()
    
    plt.subplot(222)
    f3()
    
    plt.subplot(223)
    f2()
    
    plt.show()
    return 0


main()
