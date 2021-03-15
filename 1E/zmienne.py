#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zmienne.py


def main(args):
    imie = "Julia"
    print(imie)
    print(type(imie))
    
    wiek = 16
    print(wiek)
    print(type(wiek))
    
    ocena1 = 3
    ocena2 = 5
    ocena3 = 2
    
    ocena1 = int(input("Podaj ocenę: "))
    ocena2 = 5
    ocena3 = 2    
    
    srednia = (ocena1 + ocena2 + ocena3) / 3
    print(srednia)
    print(type(srednia))

    print("Witaj", imie, ", masz", wiek, "lat!")
    print(f"Witaj {imie}, masz {wiek} lat!")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
