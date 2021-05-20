import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 2, 100)
    
    fig, ax = plt.subplots()
    ax.plot(x, x, label="linearna")
    ax.plot(x, x**2, label="kwadratowa")
    ax.plot(x, x**3, label="sześcienna")
    ax.set_title("Wykresy funkcji")
    ax.set_xlabel("etykiety x")
    ax.set_ylabel("etykiety y")
    ax.legend()
    

    #plt.plot(x, x, label='linear')
    #plt.plot(x, x**2, label='quadratic')  # etc.
    #plt.plot(x, x**3, label='cubic')
    #plt.xlabel('x label')
    #plt.ylabel('y label')
    #plt.title("Simple Plot")
    #plt.legend()
    
    plt.show()
    return 0
    

main()
