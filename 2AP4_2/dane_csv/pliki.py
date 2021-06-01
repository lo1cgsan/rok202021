import csv
import random
import numpy as np
import json


def czytaj_dane(plik, separator=','):
    dane = []
    with open(plik) as plik_csv:
        for rekord in csv.reader(plik_csv, delimiter=separator):
            dane.append(rekord)
    return dane


def zapisz_dane(plik, dane):
    with open(plik, 'w') as plik_json:
        json.dump(dane, plik_json)


def losujPunkty():
    n = int(input("Ile ruchów? "))
    x = y = 0
    lx = [0]
    ly = [0]

    for i in range(0, n):
        # wylosuj kąt i zamień go na radiany
        rad = float(random.randint(0, 360)) * np.pi / 180
        x = x + np.cos(rad)  # wylicz współrzędną x
        y = y + np.sin(rad)  # wylicz współrzędną y
        # print(x, y)
        lx.append(x)
        ly.append(y)

    print(lx, ly)

    # oblicz wektor końcowego przesunięcia
    s = np.fabs(np.sqrt(x**2 + y**2))
    print("Wektor przesunięcia:", s)

    dane = {'lx': lx, 'ly': ly, 's': s}
    zapisz_dane('ruchy_browna.json', dane)
    

def main():
    print(czytaj_dane('dane_klasa1A.csv', ';'))
    losujPunkty()


main()
