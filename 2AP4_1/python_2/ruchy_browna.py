#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import json

def rysujWykres(lx, ly, s):
    plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
    plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy Browna")
    plt.grid(True)
    plt.show()


def zapiszPunkty(dane):
    with open('rbrowna.json', 'w') as plik_json:
        json.dump(dane, plik_json)


def odczytajPunkty():
    dane = dict()
    if os.path.isfile('rbrowna.json'):
        with open('rbrowna.json', 'r') as plik_json:
            dane = json.load(plik_json)
    else:
        print('Brak pliku z danymi!')
    return dane


def losujPunkty(n):
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
    
    dane = {'x': lx, 'y': ly, 's': s}
    zapiszPunkty(dane)

    return lx, ly, s


def main():
    wybor = input(
    """
    Wybierz:
    1 - wykres zapisanych danych
    2 - wykres wylosowanych danych
    """)
    if wybor=='1':
        dane = odczytajPunkty()
        lx, ly, s = dane['lx'], dane['ly'], dane['s']
    elif wybor=='2':
        n = int(input("Ile ruchów? "))
        lx, ly, s = losujPunkty(n)
    
    rysujWykres(lx, ly, s)
    
    return 0


main()
