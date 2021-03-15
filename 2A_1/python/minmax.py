#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
#  
from random import randint

def losuj(n, MAKS):
    l = []  # pusta lista
    for i in range(n):
        l.append(randint(0, MAKS))
    return l


def min1(l, n):
    # n - 1 porównań
    min_el = l[0]
    for i in range(1, n):
        if l[i] < min_el:
            min_el = l[i]
    return min_el


def max1(l, n):
    # n - 1 porównań
    max_el = l[0]
    for i in range(1, n):
        if l[i] > max_el:
            max_el = l[i]
    return max_el


def minmax(l, n):
    # n / 2 porównań
    lmin = []
    lmax = []
    [0, 2, 4, 6, 8, 18]
    for i in range(0, n, 2):
        if l[i] > l[i + 1]:
            lmax.append(l[i])
            lmin.append(l[i + 1])
        else:
            lmax.append(l[i + 1])
            lmin.append(l[i])
    return lmin, lmax


def main(args):
    n = 21
    MAKS = 50
    lista = losuj(n, MAKS)
    print(lista)
    min_el = min1(lista, n)
    max_el = max1(lista, n)
    print(min_el, max_el)
    
    lmin, lmax = minmax(lista, n)
    print(lmin)
    print(lmax)
    n2 = int(n / 2)
    min_el = min1(lmin, n2)
    max_el = max1(lmax, n2)
    print(min_el, max_el)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
