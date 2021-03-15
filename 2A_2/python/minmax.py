#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  
from random import randint


def losuj(lista, ile, zakres):
    for i in range(ile):
        lista.append(randint(0, zakres))


def minmax1(lista):
    min = lista[0]
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < min:
            min = lista[i]
        if lista[i] > max:
            max = lista[i]
    return min, max


def main(args):
    ile = 20
    zakres = 50
    lista = []  # int lista[ile];
    losuj(lista, ile, zakres)
    print(lista)
    print(minmax1(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
