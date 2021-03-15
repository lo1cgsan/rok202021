#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reszta.py
#  
def wydajReszte1(reszta, listaNm):
    i = 0  # indeks wskazujący nominał
    while reszta > 0:
        if reszta >= listaNm[i]:
        # 25 >= 200
        # 25 >= 100
        # 25 >= 20
            ileNm = int(reszta / listaNm[i])
            reszta -= ileNm * listaNm[i]
            print(f"{ileNm} x {listaNm[i]}")
        i += 1


def wydajReszte2(reszta, listaNm):
    i = 0  # indeks wskazujący nominał
    liczbaNm = len(listaNm)  # liczba nominałów
    while reszta > 0 and i < liczbaNm:
        while i < liczbaNm and reszta < listaNm[i]:
            i += 1
        # print "aktN={}".format(aktualnyNominal)
        if i < liczbaNm and reszta >= listaNm[i]:
            ileNm = int(reszta / listaNm[i])
            reszta -= ileNm * listaNm[i]
            print(f"{ileNm} x {listaNm[i]}")

    if reszta > 0:
        print(f"Brak nominałów do wydania pozostałej kwoty: {reszta} zł")


def main(args):
    # dane wejściowe
    listaNm = [200, 10, 2]
    reszta = int(input("Podaj resztę: "))
    wydajReszte2(reszta, listaNm)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
