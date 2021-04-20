import matplotlib.pyplot as plt


def main():
    """
    wykres funkcji a * x + b
    """
    a = 1
    b = 2
    
    x = range(-10, 11)
    y = [a * i + b for i in x]
    #for i in x:
    #    y.append(a * i + b)
    
    print(list(x))
    print(y)
    
    plt.grid(True)
    plt.title('Wykres f(x) = a*x + b')
    plt.xticks(range(-10, 11, 2))
    plt.yticks(y)
    # plt.plot(x, y, "g*:")
    plt.plot(x, y, color='r', marker='^', ls='dashed', lw=3)
    plt.show()
    return 0
    
    
main()
