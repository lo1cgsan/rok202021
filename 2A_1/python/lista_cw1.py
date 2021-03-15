#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lista_01.py
#
#  Program pobiera od użytkownika określoną przez niego liczbę ocen
#  i zapisuje je w liście. Następnie liczy ich średnią i drukuje wynik.
#  Pobieranie danych powinna realizować funkcja pobierz(), obliczanie średniej
# – funkcja obliczSrednia(), drukowanie wyniku w funkcji głównej.
#
def pobierz(l, ile):
    ocena = 0;
    while ile > 0:
        ocena = int(input("Podaj ocenę: "))
        if ocena > 0 and ocena < 7:
            l.append(ocena)  # dołączenie elementu do listy
            ile -= 1
        else:
            print("Błędne dane!")


def obliczSrednia(l):
    suma = 0
    for ocena in l:
        suma += ocena
    return suma / len(l)


def main(args):
    lista = []  # pusta lista
    ile = int(input("Ile podasz ocen? "))
    
    pobierz(lista, ile)

    print("Średnia ocen:", obliczSrednia(lista))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
