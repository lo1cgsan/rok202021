import matplotlib.pyplot as plt
import numpy as np
import random


def wykres(lx, ly, s):
    plt.grid()
    plt.legend([f"Dane x, y\nPrzemieszczenie: {s}"], loc="upper left")
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.xticks(range(min(lx), max(lx) + 1, 2))
    plt.yticks(range(min(ly), max(ly) + 1, 2))
    plt.title("Rouchy Browna")
    plt.plot(lx, ly, "go:", linewidth=2)
    plt.show()


def main():
    n = int(input("Ile ruchów? "))
    x = y = 0
    r = 5
    lx = [x]
    ly = [y]
    for i in range(n):
        # wylosuj kąt wyrażony w radianach
        kat = random.randint(0, 360) * np.pi / 360
        x = x + np.cos(kat) * r
        y = y + np.sin(kat) * r
        # print(x, y)
        lx.append(int(np.floor(x)))
        ly.append(int(np.floor(y)))
        
    print(lx)
    print(ly)
    s = np.sqrt(x**2 + y**2)
    print("Wektor przesunięcia:", s)
    
    wykres(lx, ly, s)
    return 0


main()
