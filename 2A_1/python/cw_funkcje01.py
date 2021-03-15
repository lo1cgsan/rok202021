#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw_funkcje01.py
#  

def drukuj(staz, zarobek):
    # print("Pracujesz", staz, "lat.")
    print(f"Pracujesz {staz} lat.")
    print(f"Zarabiasz {zarobek} zł.")


def awans(staz, zarobek):
    staz += 1
    zarobek = zarobek + 0.1 * zarobek
    return staz, zarobek


def main(args):
    staz = 1
    zarobek = 1000
    lata = int(input("Ile lat będziesz pracował? "))
    for i in range(lata):
        drukuj(staz, zarobek)
        staz, zarobek = awans(staz, zarobek)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
