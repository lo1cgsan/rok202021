#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
import math  # import biblioteki matematycznej


def licz_pole(a, b):
    # a = float(input("Podaj bok 1: "))
    # b = float(input("Podaj bok 2: "))
    pole = a * b
    print(f"Pole wynosi: {pole}.")


def licz_obwod(a, b):
    # a = float(input("Podaj bok 1: "))
    # b = float(input("Podaj bok 2: "))    
    obwod = 2 * (a + b)
    print(f"Obwód wynosi: {obwod}.")


def licz_pole_kolo():
    r = float(input("Podaj promień: "))
    pole = math.pi * r**2
    print(f"Pole wynosi: {pole}.")
    

def main():
    a = float(input("Podaj bok 1: "))
    b = float(input("Podaj bok 2: "))
    licz_pole(a, b)
    licz_obwod(a, b)
    licz_pole_kolo()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
