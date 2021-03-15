#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje02.py
#  

licz1 = int(input("Podaj liczbę: "))  # zmienna globalna
licz2 = int(input("Podaj liczbę: "))  # zmienna globalna

def sumuj(l1, l2):
    """
    Funkcja sumuje dwie podane liczby i drukuje wynik.
    """
    suma = l1 + l2  # zmienne lokalne
    print("Suma:", suma)


def sumuj2():
    print("Suma:", licz1 + licz2)


def main(args):
    # global licz1, licz2
    licz1 = 0
    licz2 = 3
    
    print("Suma:", licz1 + licz2)
    sumuj2()  # wywołanie funkcji
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
