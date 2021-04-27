import matplotlib.pyplot as plt

def funkcja1():
    """
    x = <-10, 10>
    f(x) = a * x + b
    """
    a = float(input("Podaj współczynnik a: "))
    b = float(input("Podaj współczynnik b: "))
    # [-10, -9, -8 ... 8, 9, 10]
    x = list(range(-10, 11, 2))
    y = [a * i + b for i in x]
    #for i in x:
    #    y.append(a * i + b)
    print(x)
    print(y)
    
    plt.grid()
    plt.xticks(x)
    plt.yticks(y)
    plt.title(f"f(x) = {a} * x + {b}")
    #[color][marker][linestyle]
    plt.plot(x, y, "cv:")
    plt.show()


def main():
    funkcja1()
    return 0
    
    
main()
