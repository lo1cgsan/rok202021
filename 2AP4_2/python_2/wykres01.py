import matplotlib.pyplot as plt


def funkcja1():
    """
    x = <-10, 10>
    y = a * x + b
    """
    a = int(input("Podaj współczynnik a: "))
    b = int(input("Podaj wspłczynnik b: "))

    x = list(range(-10, 11))
    # [-10, -9, -8 ... 8, 9, 10]
    y = []
    for i in x:
        y.append(a * i + b)
        
    print(x)
    print(y)
    
    plt.grid()
    plt.xticks(x)
    plt.plot(x, y, "r^:")
    plt.show()


def main():
    funkcja1()
    return 0


main()
