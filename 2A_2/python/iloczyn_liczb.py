#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  iloczyn_liczb.py
#  
#  Program liczy iloczyn 10 liczb pobranych od użytkownia.
#
#  Przykład algorytmu iteracyjnego

def main(args):
    iloczyn = 1
    for i in range(10):
        a = int(input("Podaj liczbę: "))
        iloczyn = iloczyn * a
        
    print(iloczyn)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
