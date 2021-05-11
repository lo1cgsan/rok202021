import numpy as np
import matplotlib.pyplot as plt


def f1(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


def f2(t):
    return np.cos(2 * np.pi * t)


def f3(t):
    return np.sin(2 * np.pi * t)


def main():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    
    plt.subplot(224)
    plt.grid()
    plt.title("Wykres 1")
    plt.plot(t1, f(t1))
    
    plt.subplot(221)
    plt.plot(t2, f2(t2))
    
    plt.subplot(223)
    plt.plot(t2, f3(t2))
    
    plt.show()
    return 0


main()
