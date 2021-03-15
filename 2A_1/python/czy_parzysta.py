#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  czy_parzysta.py
  

def main(args):
    liczba = int(input("Podaj liczbę: "))
    if liczba % 2 == 0:
        print("liczba parzysta")
    else:
        print("liczba nieparzysta")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
