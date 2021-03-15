#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_parzyste.py
#  
#  Program sumuje liczby parzyste z wygenerowanego zakresu


def main(args):
    suma = 0
    start = int(input("Podaj początek zakresu: "))
    koniec = int(input("Podaj koniec zakresu: "))
    
    for liczba in range(start, koniec + 1):
        print(liczba)
        if liczba % 2 == 0:
            suma = suma + liczba

    print("Suma =", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
