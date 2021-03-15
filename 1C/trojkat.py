#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py

def czyTrojkat(a, b, c):
    """
    Funkcja sprawdza czy z podanych boków można zbudować trójkąt.
    """
    if a + b > c and a + c > b and b + c > a:
        print("Wszystkie warunki są prawdziwe!")
        print("Da się!")
    else:
        print("Nie da się!")


def main():
    # Dane wejściowe
    a = int(input("Podaj bok a: "))
    b = int(input("Podaj bok b: "))
    c = int(input("Podaj bok c: "))
    
    # Wywołanie funkcji
    czyTrojkat(a, b, c)
    return 0

main()
