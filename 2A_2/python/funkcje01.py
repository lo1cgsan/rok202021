#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje01.py
#  

def sumuj(a, b):  # definicja funkcji z parametrami
    suma = a + b
    print("Suma:", suma)


def odejmij(a, b):
    roznica = a - b
    print("Różnica:", roznica)


def potega(podstawa, wykladnik):
    wynik = podstawa**wykladnik  # użycie operatora potęgowania
    return wynik


def main(args):
    liczba1 = int(input("Podaj liczbę: "))
    liczba2 = int(input("Podaj liczbę: "))
    # sumuj(liczba1, liczba2)  # wywołanie funkcji z argumentami
    # odejmij(liczba1, liczba2)
    wynik = potega(liczba1, liczba2)
    print(wynik)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
