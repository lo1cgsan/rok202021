def czy_na_prostej(xp, yp, a, b):
    z = a * xp + b
    return yp == z


def main():
    xp = int(input("Współrzędna x: "))
    yp = int(input("Współrzędna y: "))
    a = float(input("Współczynnik a: "))
    b = float(input("Współrzędna b: "))
    
    if czy_na_prostej(xp, yp, a, b):
        print("Punkt na prostej")
    else:
        print("Punkt poza prostą")
    return 0
    
    
main()
