#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oceny.py
#  
def pobierz_oceny(ile):
    oceny = []
    for i in range(ile):
        ocena = int(input(f"Podaj ocenę {i + 1}: "))
        if ocena > 0 and ocena < 7:
            oceny.append(ocena)
        else:
            print("Błędne dane!")

    srednia = sum(oceny) / len(oceny)
    print(f"Średnia {ile} ocen: {srednia}")


def main(args):
    ile = 5
    pobierz_oceny(ile)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
