#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  horner.py
#  

def drukujw(n, tbwsp):
    for i in range(n):
        print(f"{tbwsp[i]}x^{n - i} + ", end="")
    print(tbwsp[n])


def horner_it(n, tbwsp, x):
    # x * (x * (x * a0 + a1) + a2) + a3
    # 2 * (2 * (2 * 2 + 3) + 5) + 2
    wynik = tbwsp[0]
    for i in range(1, n + 1):
        wynik = x * wynik + tbwsp[i]
    return wynik


def horner_rek(n, tbwsp, x):
    if n < 1:
        return tbwsp[0]
    else:
        return x * horner_rek(n - 1, tbwsp, x) + tbwsp[n]
    


def main(args):
    n = int(input("Stopień: "))
    tbwsp = []
    for i in range(n + 1):
        tbwsp.append(float(input(f"Współczynnik przy potędze {n - i}: ")))
    x = float(input("Argument: "))
    
    print("Wartość wielomianu o postaci:")
    drukujw(n, tbwsp)
    print(f"wynosi: {horner_it(n, tbwsp, x)}")
    print(f"wynosi: {horner_rek(n, tbwsp, x)}")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
