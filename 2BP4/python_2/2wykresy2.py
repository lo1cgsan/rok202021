import numpy as np
import matplotlib.pyplot as plt


def f1():
    lx = np.arange(0.0, 5.0, 0.1)
    plt.grid()
    plt.plot(lx, np.exp(-lx), 'k')

    

def f2():
    lx = np.arange(0.0, 5.0, 0.02)
    plt.title("sin(x)")
    plt.plot(lx, np.sin(2 * np.pi * lx), 'r')



def f3():
    lx = np.arange(0.0, 5.0, 0.02)
    plt.title("cos(x)")
    plt.plot(lx, np.cos(2 * np.pi * lx), 'r')
    plt.legend("cos(x)")


def main():
    plt.figure(1)
    fig = plt.gcf()
    fig.set_size_inches(8, 10)
    
    plt.subplot(311)
    f1()
    
    plt.subplot(312)
    f2()

    plt.subplot(313)
    f3()

    plt.show()
    return 0


main()
