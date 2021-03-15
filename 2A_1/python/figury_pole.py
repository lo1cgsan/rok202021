#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_pole.py


def main(args):
    bok1 = input("Podaj 1 bok: ")
    bok2 = input("Podaj 2 bok: ")
    print("Obwód:", 2 * int(bok1) + 2 * int(bok2))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
