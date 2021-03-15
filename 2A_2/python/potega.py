#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py

def potega1(p, w):
    wynik = 1
    for i in range(w):
    # for (int i = 0; i < w; i++) w C++
        wynik = wynik * p
    return wynik


def potega_rek(p, w):
    if w == 0:
        return 1
    else:
        return potega_rek(p, w - 1) * p


def main(args):
    p = int(input("Podaj podstawę: "))
    w = int(input("Podaj wykładnik: "))
    print(f"{p} do potęgi {w} =", potega1(p, w))
    print(f"{p} do potęgi {w} =", potega_rek(p, w))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
