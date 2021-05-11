import numpy as np
import matplotlib.pyplot as plt


def f1():
    lx = np.arange(0.0, 5.0, 0.1)
    ly = [np.exp(-x) * np.cos(2 * np.pi * x) for x in lx]
    plt.grid()
    plt.title("Wykres 1")
    plt.plot(lx, ly, 'k')


def f2():
    lx = np.arange(0.0, 5.0, 0.02)
    ly = [np.cos(2 * np.pi * x) for x in lx]
    plt.legend("f(cos(x))")
    plt.plot(lx, ly, 'r--')


def f3():
    lx = np.arange(0.0, 5.0, 0.02)
    ly = [np.sin(2 * np.pi * x) for x in lx]
    plt.legend("f(sin(x))")
    plt.plot(lx, ly, 'go')    


def main():
    plt.subplot(221)
    f2()
    
    plt.subplot(223)
    f3()
    
    plt.subplot(222)
    f1()
    
    plt.show()
    return 0


main()
