def poleT(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))


def main():
    # współrzędne badanego punktu
    xp = float(input("Podaj współrzędną x: "))
    yp = float(input("Podaj współrzędną y: "))
    # współrzędne lewego wierzchołka
    x1 = float(input("Podaj współrzędną x1: "))
    y1 = float(input("Podaj współrzędną y1: "))
    # współrzędne górnego wierzchołka
    x2 = float(input("Podaj współrzędną x2: "))
    y2 = float(input("Podaj współrzędną y2: "))
    # współrzędne prawego wierzchołka
    x3 = float(input("Podaj współrzędną x3: "))
    y3 = float(input("Podaj współrzędną y3: "))
    
    poleG = poleT(x1, y1, x2, y2, x3, y3)
    poleT1 = poleT(x1, y1, x2, y2, xp, yp)
    poleT2 = poleT(x2, y2, x3, y3, xp, yp)
    poleT3 = poleT(x1, y1, x3, y3, xp, yp)
    
    if poleG == poleT1 + poleT2 + poleT3:
        print("Punkt należy do trójkąta.")
    else:
        print("Punkt nie należy do trójkąta.")

    return 0


main()
