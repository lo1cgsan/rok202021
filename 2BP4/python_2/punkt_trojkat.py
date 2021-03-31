def pole(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))


def main():
    # współrzędne punktu P
    xp = int(input("Współrzędna x: "))
    yp = int(input("Współrzędna y: "))
    # współrzędne wierzchołka A
    x1 = int(input("Współrzędna x1: "))
    y1 = int(input("Współrzędna y1: "))
    # współrzędne wierzchołka B
    x2 = int(input("Współrzędna x2: "))
    y2 = int(input("Współrzędna y2: "))
    # współrzędne wierzchołka C
    x3 = int(input("Współrzędna x3: "))
    y3 = int(input("Współrzędna y3: "))
    
    poleT = pole(x1, y1, x2, y2, x3, y3)
    poleT1 = pole(x1, y1, x2, y2, xp, yp)
    poleT2 = pole(x2, y2, x3, y3, xp, yp)
    poleT3 = pole(x1, y1, xp, yp, x3, y3)
    
    if poleT == poleT1 + poleT2 + poleT3:
        print("Punkt wewnątrz")
    else:
        print("Punkt na zewnątrz")
    return 0


main()
