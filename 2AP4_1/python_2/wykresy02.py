import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    x = <-10, 10> z krokiem 0.5
    f(x) = x/-3 + a dla x <= 0
    f(x) = x*x/3 dla x >= 0
    """
    a = int(input("Podaj współczynnik: "))
    x = np.arange(-10, 10, 0.5)
    
    y1 = []
    y2 = []
    for i in x:
        if i <= 0:
           y1.append(i / -3 + a)
        else:
           y2.append(i * i / 3)
    
    print(x)
    print(y1)
    print(y2)
    
    return
    plt.grid(True)
    plt.title('Wykres f(x) = a*x + b')
    plt.xticks(range(-10, 11, 2))
    plt.yticks(y)
    # plt.plot(x, y, "g*:")
    plt.plot(x, y, color='r', marker='^', ls='dashed', lw=3)
    plt.show()
    return 0
    
    
main()
