#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oceny.py


def pobierz_oceny(ile):
    oceny = []  # pusta lista
    for i in range(ile):
        ocena = int(input("Podaj ocenę? "))
        if ocena > 0 and ocena < 7:
            oceny.append(ocena)
        else:
            print("Błędne dane!")

    print(oceny)
    srednia = sum(oceny) / ile
    print(f"Średnia z {ile} ocen: {srednia}")


def main():
    ile = int(input("Ile podasz ocen? "))
    pobierz_oceny(ile)
    return 0


main()
