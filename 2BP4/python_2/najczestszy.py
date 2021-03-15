#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  najczestszy.py
#  
from random import randint


def losuj(n, zakres):
    lista = []
    for i in range(n):
        lista.append(randint(0, zakres))
    print(lista)
    return lista


def policz_elementy(lista):
    slownik = {}
    for i in lista:
        if i not in slownik:
            licznik = 0
            for j in lista:
                if i == j:
                    licznik += 1
            slownik[i] = licznik

    print(slownik)


def main(args):
    n = 20
    zakres = 20
    lista = losuj(n, zakres)
    policz_elementy(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
