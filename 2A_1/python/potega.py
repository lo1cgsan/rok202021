#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  

def potega_it(p, w):
    wynik = 1
    for i in range(w):
        wynik = wynik * p
    return wynik


def main(args):
    podstawa = int(input("Podaj podstawę: "))
    wykladnik = int(input("Podaj wykładnik: "))
    print("Wynik:", potega_it(podstawa, wykladnik))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
