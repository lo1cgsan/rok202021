def funkcja(a, b, x):
    return a * x + b


def main():
    a = float(input("Podaj współczynnik a: "))
    b = float(input("Podaj współczynnik b: "))
    xp = float(input("Podaj współrzędną x: "))
    yp = float(input("Podaj współrzędną y: "))
    
    z = a * xp + b
    if z == yp:
        print(f"Punkt ({xp},{yp}) należy do prostej.")
    else:
        print(f"Punkt ({xp},{yp}) nie należy do prostej.")
    return 0


main()
