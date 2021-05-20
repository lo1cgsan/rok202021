import numpy as np
import matplotlib.pyplot as plt


def wykres1():
    x = np.linspace(0, 2, 50)
    plt.plot(x, x, label='liniowa')
    

def wykres2():
    x = np.linspace(0, 2, 50)
    plt.plot(x, x**2, label='kwadratowa')


def wykres3():
    x = np.linspace(0, 2, 50)
    plt.plot(x, x**3, label='sześcienna')


def main():
    wykres1()
    wykres2()
    wykres3()
    plt.legend()
    plt.show()
    return 0


main()
