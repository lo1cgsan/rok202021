import random
import numpy as np
import matplotlib.pyplot as plt


def wykres(lx, ly, s):
    
    plt.grid()
    plt.title("Ruchy Browna")
    plt.text(0.2, 0.2, "(0, 0)")
    plt.plot(lx, ly, "go:")
    plt.legend([f"Przesunięcie: {s:.3f}"])
    plt.show()


def main():
    n = int(input("Ile ruchów? "))
    x = y = 0
    r = 2
    lx = [0]
    ly = [0]
    for i in range(n):
        kat = random.randint(0, 360) * np.pi / 180
        x = x + np.cos(kat) * r
        y = y + np.sin(kat) * r
        lx.append(x)
        ly.append(y)
        print(kat, x, y)

    s = np.sqrt(x**2 + y**2)
    print(f"Przesunięcie: {s:.3f}")

    wykres(lx, ly, s)
    return 0


main()
