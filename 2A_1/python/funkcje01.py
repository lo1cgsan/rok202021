#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje01.py
#  

def sumuj(l1, l2):
    """
    Funkcja sumuje dwie podane liczby i drukuje wynik.
    """
    suma = l1 + l2
    print("Suma:", suma)


def odejmij(l1, l2):
    """
    Funkcja odejmuje dwie podane liczby i drukuje wynik.
    """
    roznica = l1 - l2
    print("Różnica:", roznica)


def pomnoz(l1, l2):
    """
    Funkcja mnozy dwie liczby i zwraca wynik.
    """
    iloczyn = l1 * l2
    return iloczyn


def main(args):
    liczba1 = int(input("Podaj liczbę: "))
    liczba2 = int(input("Podaj liczbę: "))
    
    # sumuj(liczba1, liczba2)  # wywołanie funkcji
    # odejmij(liczba1, liczba2)  # wywołanie funkcji
    
    print("Iloczyn:", pomnoz(liczba1, liczba2))
    # wynik = pomnoz(liczba1, liczba2)
    # print("Iloczyn:", wynik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
