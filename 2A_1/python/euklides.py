#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
#  

def euklides1(a, b):
    licznik = 0
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        licznik = licznik + 1
    print("Powtórzeń:", licznik)
    return a


def euklides_rek1(a, b):
    if a == b:
        return a
    if a > b:
        return euklides_rek(a - b, b)
    else:
        return euklides_rek(a, b - a)


def euklides2(a, b):
    licznik = 0 
    while a > 0:
        a = a % b
        b = b - a
        licznik = licznik + 1
    print("Powtórzeń:", licznik)
    return b


def euklides_rek2(a, b):
    pass


def main(args):
    #a = int(input("Podaj liczbę: "))
    #b = int(input("Podaj liczbę: "))
    #print(f"NWD({a}, {b}) =", euklides1(a, b))
    #print(f"NWD({a}, {b}) =", euklides2(a, b))
    #assert(euklides_rek(a, b) == euklides1(a, b))
    assert(euklides_rek1(25, 6) == 1)
    assert(euklides1(14, 6) == 2)
    assert(euklides2(14, 6) == 2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
