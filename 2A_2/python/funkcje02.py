#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje02.py
#  

a = int(input("Podaj liczbę 1: "))  # zmienna globalna
b = int(input("Podaj liczbę 2: "))  # zmienna globalna

def sumuj(a, b):
    suma = a + b
    print("Suma:", suma)


def sumuj2():
    suma = a + b
    print("Suma:", suma)


def main(args):
    l1 = int(input("Podaj liczbę 3: "))  # zmienna lokalna
    l2 = int(input("Podaj liczbę 4: "))
    sumuj(a, b)
    sumuj2()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
