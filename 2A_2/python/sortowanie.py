#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sortowanie.py
#  
from random import randint

def losuj(n, zakres):
    liczby = []
    for i in range(n):
        liczby.append(randint(0, zakres))
    return liczby


def sortuj_wybor(liczby, n):
    for i in range(n):
        k = i
        for j in range(i, n):
            if liczby[j] < liczby[k]:  # wyszukiwanie najmniejszej liczby
                k = j
        tmp = liczby[i]
        liczby[i] = liczby[k]
        liczby[k] = tmp


def sort_bubble(liczby,n):
    """
    n – ilość liczb w liście
    n – 1 iteracji pętli zewnętrznej
    """
    for i in range(n - 1, 0, -1):
        print(i)
        for j in range(i):
            if liczby[j] > liczby[j + 1]:
                liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]


def sort_insert(liczby, n):
   #  ~[4, 7, 1, 2, 9, 0]
   # ~1[4, 7, 1, 2, 9, 0]
   # ~2[1, 4, 7, 2, 9, 0]
   # ~3[1, 2, 4, 7, 9, 0]
   # ~4[1, 2, 4, 7, 9, 0]
   # ~5[0, 1, 2, 4, 7, 9]
    for i in range(1, n):
        el = liczby[i]
        j = i - 1
        while j >= 0 and liczby[j] > el:
            liczby[j + 1] = liczby[j]
            j = j - 1
        liczby[j + 1] = el  # wstawianie elementu


def main(args):
    n = 10
    zakres = 30
    liczby = losuj(n, zakres)
    print(liczby)
    sort_insert(liczby, n)
    print(liczby)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
