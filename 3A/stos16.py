#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos16.py

dane = ([0]) * 5
rozmiar = 0


def wyswietl_stos():
    global dane, rozmiar
    print("Zawartość stosu:")
    for i in range(rozmiar, 0, -1):
        print(dane[i])
    if rozmiar == 0:
        print("Stos jest pusty!")


def push():
    global dane, rozmiar
    if rozmiar >= 5:
        print("Stos pełny!")
    else:
        rozmiar += 1
        dane[rozmiar] = int(input("PUSH (podaj liczbę): "))


def pop():
    global dane, rozmiar
    if rozmiar >= 1:
        print("POP (usunięcie liczby ze stosu):", dane[rozmiar])
        rozmiar -= 1
    else:
        print("Stos pusty!")


def size():
    global rozmiar
    print("Liczba elementów na stosie:", rozmiar)


def empty():
    global dane, rozmiar
    if rozmiar == 0:
        print("EMPTY: Stos pusty! True")
    else:
        print("EMPTY: Stos niepusty! False")


def main(args):
    while True:
        wyswietl_stos()
        print("""
              Menu główne:
              1. PUSH
              2. POP
              3. SIZE
              4. EMPTY
              5. Koniec
              """)
        wybor = int(input("Wybór: "))
        if wybor == 1:
            push()
        elif wybor == 2:
            pop()
        elif wybor == 3:
            size()
        elif wybor == 4:
            empty()
        else:
            break
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
