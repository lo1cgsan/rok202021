#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_parzyste.py
#  
#  Program sumuje liczby parzyste w zakresie <0, 100>
#
#  Przykład algorytmu iteracyjnego oraz warunkowego

def main(args):
    start = int(input("Podaj liczbę początkową: "))
    koniec = int(input("Podaj liczbę końcową: "))
    suma = 0
    for liczba in range(start, koniec + 1):
        if liczba % 2 == 0:
            suma = suma + liczba
    print(suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
