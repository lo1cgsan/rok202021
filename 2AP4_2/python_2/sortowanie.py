#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sortowanie.py


def sort_bubble(lista, n):
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp


def main():
    n = 8
    lista = [6, 5, 3, 1, 8, 7, 2, 4]
    print(lista)
    sort_bubble(lista, n)
    print(lista)
    return 0


main()

# ~if __name__ == '__main__':
    # ~import sys
    # ~sys.exit(main(sys.argv))
