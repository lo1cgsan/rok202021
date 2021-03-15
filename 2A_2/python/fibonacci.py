#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fibonacci.py
#  

def fib_1(n):
    pwyrazy = (0, 1)  #dwa pierwsze wyrazy zapisane w tupli
    a, b = pwyrazy  #przypisanie wielokrotne
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
#    [a, b]
#       [a, b]
#          [a, b]
    while a < n:
        print(b)
        a, b = b, a + b  #przypisanie wielokrotne


def fib_2(n):
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    wynik, a, b = 0, 0, 1
    if n < 2:
        return n
    for i in range(1, n):
        wynik = a + b
        a = b
        b = wynik
        # a, b = b, wynik
    return wynik


def fib_rek(n):
    if n < 2:
        return n
    return fib_rek(n - 1) + fib_rek(n - 2)


def main(args):
    n = int(input("Podaj numer wyrazu: "))
    #fib_1(n)
    #for i in range(2, n + 1):
    # print(f"fib_2({i}) = {fib_2(i)}, {fib_2(i)/fib_2(i - 1)}")
    print(f"fib_2({n}) = {fib_2(n)}")
    print(f"fib_rek({n}) = {fib_rek(n)}")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
