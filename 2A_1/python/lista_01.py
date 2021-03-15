#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lista_01.py


def main(args):
    lista = []  # pusta lista
    ile = int(input("Ile podasz ocen? "))
    
    for i in range(ile):
        ocena = int(input("Podaj ocenę: "))
        lista.append(ocena)  # dołączenie elementu do listy

    lista.append(input("Wpisz coś jeszcze: "))

    for i in range(len(lista)):  # dostęp do listy za pomocą indeksów
        print(lista[i], end=' ')

    print()
    for ocena in lista:
        print(ocena, end=' ')


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
