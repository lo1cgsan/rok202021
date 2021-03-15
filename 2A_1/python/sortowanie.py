#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sortowanie.py
#  
import random
# k = 0
# a = [4, 7, 1, 0, 10]
# i = 0, k = 3
# a = [0| 7, 1, 4, 10]
# i = 1, k = 2
# a = [0, 1| 7, 4, 10]
# i = 2, k = 3
# a = [0, 1, 4| 7, 10]
# i = 3, k = 3
# a = [0, 1, 4, 7| 10]

def sort_wybor(liczby, n):
    for i in range(n):
        k = i
        for j in range(i, n):
            if liczby[j] < liczby[k]:
                k = j
        el = liczby[i]
        liczby[i] = liczby[k]
        liczby[k] = el
        # liczby[i], liczby[k] = liczby[k], liczby[i]



def sort_bubble(l, n):
# [6, 5, 3, 1, 8, 7, 2, 4]
# n = 8, i = 7, j = 0 -> 6
    for i in range(n - 1, 0, -1):
        for j in range(i):
            # print(j, i)
            if l[j] < l[j + 1]:
                el = l[j]
                l[j] = l[j + 1]
                l[j + 1] = el
                #l[j], l[j + 1] = l[j + 1], l[j]


def sort_insert(l, n):
    for i in range(1, n):



def generuj_liste(n, zakres):
    liczby = []
    for i in range(n):
        liczby.append(random.randint(0, zakres))
    return liczby


def main(args):
    n = 20
    zakres = 20
    liczby = generuj_liste(n, zakres)
    print(liczby)
    # sort_wybor(liczby, n)
    sort_bubble(liczby, n)
    print(liczby)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
