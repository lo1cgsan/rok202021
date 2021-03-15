#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  listy_cw1.py
#  

def pobierzOceny(lista, ile):
    while ile > 0:
        ocena = int(input("Podaj ocenę: "))
        if ocena > 0 and ocena < 7:
            lista.append(ocena)
            ile -= 1
        else:
            print("Błędne dane!")

def obliczSrednia(lista):
    suma = 0
    for ocena in lista:
        suma += ocena
    return suma / len(lista)
    # return sum(suma) / len(lista)

def main(args):
    ile = int(input("Ile ocena podasz? "))
    lista = []  # pusta lista
    pobierzOceny(lista, ile)
    
    print(lista)
    
    print("Średnia:", obliczSrednia(lista))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
