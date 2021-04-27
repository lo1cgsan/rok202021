import random
import numpy as np
import matplotlib.pyplot as plt


def wykres(lx, ly, s):
    plt.grid()
    plt.plot(lx, ly, "go:")
    plt.show()


def main():
    n = int(input("Ile ruchów? "))
    # współrzędne określające położenie cząsteczki
    x = y = 0
    # stała długość ruchu cząsteczki
    r = 1

    lx = [0]
    ly = [0]

    for i in range(n):
        kat = random.randint(0, 360) * np.pi / 180
        x = x + np.cos(kat) * r
        y = y + np.sin(kat) * r
        lx.append(x)
        ly.append(y)
        print(kat, x, y)

    # końcowe przesunięcie
    s = np.sqrt(x**2 + y**2)
    print("Końcowe przesunięcie:", s)
    
    wykres(lx, ly, s)
    return 0
    
    
main()
