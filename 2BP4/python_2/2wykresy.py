import numpy as np
import matplotlib.pyplot as plt


def f1(t):
    return np.exp(-t)
    

def main():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    
    plt.subplot(224)
    plt.grid()
    plt.plot(t1, f1(t1))
    
    plt.subplot(211)
    plt.title("Wykres f(cos(x))")
    plt.plot(t2, np.cos(2 * np.pi * t2))
    
    
    plt.subplot(223)
    plt.title("Wykres f(sin(x))")
    plt.plot(t2, np.sin(2 * np.pi * t2))

    plt.show()
    return 0


main()
