def funkcja(a, b, x):
    return a * x + b

def main():
    xp = int(input("Podaj współrzędną x: "))
    yp = int(input("Podaj współrzędną y: "))
    a = float(input("Podaj współczynnik a: "))
    b = float(input("Podaj współczynnik b: "))
    
    z = a * xp + b
    if yp == z:
        print("Punkt przynależy.")
    else:
        print("Punkt nie przynależy.")
    return 0


main()
