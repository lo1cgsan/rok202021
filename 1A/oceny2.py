#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oceny2.py
#  

def pobierzOceny(ile = 5):
    oceny = []  # definicja pustej listy
    for i in range(ile):
        ocena = int(input("Podaj ocenę: "))
        if ocena > 0 and ocena < 7:
            oceny.append(ocena)
        else:
            print("Błędne dane!")
    
    srednia = sum(oceny) / len(oceny)
    print(f"Podano {len(oceny)} ocen. Średnia: {srednia}")


def main(args):
    pobierzOceny()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
