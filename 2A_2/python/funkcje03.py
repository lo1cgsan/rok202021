#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje02.py
#  

def zwieksz(a):
    a += 2  # powiększenie wartości o dwa, tj: a = a + 2
    print(a)


def zwieksz2(b):
    b[0] += 2
    print(b)


def main(args):
    a = int(input("Podaj liczbę: "))  # zmienna lokalna
    print(a)
    zwieksz(a)
    print(a)
    
    b = [1];  # lista 1-elementowa
    b[0] = int(input("Podaj liczbę: "))
    zwieksz2(b)
    print(b)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
