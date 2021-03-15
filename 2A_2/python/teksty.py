#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  teksty.py


def main(args):
    litera = "z"
    znaki = input("Podaj tekst: ")
    print(znaki[len(znaki)-1])  # drukowanie ostatniego znaku
    print(znaki[-1])  # drukowanie ostatniego znaku
    for znak in znaki:
        print(ord(znak))
    print()
    print(chr(65))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
