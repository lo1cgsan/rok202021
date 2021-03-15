#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#  
# n! = 1 dla n = 0
# n! = n * (n-1)! dla n >= 1

# ~4! = 4 * 3!
# ~3! = 3 * 2!
# ~2! = 2 * 1!
# ~1! = 1 * 0!
# ~0! = 1
# ~1! = 1 * 1
# ~2! = 2 * 1
# ~3! = 3 * 2
# ~4! = 4 * 6

def silnia_rek(n):
    if n < 1:
        return 1
    return silnia_rek(n-1) * n
    

def main(args):
    n = int(input("Podaj liczbę: "))
    print(f"{n}! =", silnia_rek(n))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
