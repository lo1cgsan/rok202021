#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reszta.py
  
import turtle

def rysuj_it(ile, dlbok, kat):
    for i in range(ile):
        turtle.forward(dlbok)
        turtle.right(kat)
    

def rysuj_rek(ile, dlbok, kat):
    if ile < 1:
        return
    turtle.forward(dlbok)
    turtle.right(kat)
    rysuj_rek(ile - 1, dlbok, kat)


def rysuj_rek2(ile, dlbok, kat):
    if ile < 1:
        return
    turtle.forward(dlbok)
    turtle.right(kat)
    turtle.forward(dlbok + dlbok//2)
    turtle.right(kat)
    rysuj_rek(ile - 1, dlbok + dlbok//2, kat)


def main(args):
    turtle.setup(800, 600)
    # rysuj_it(4, 100, 90)
    rysuj_rek2(20, 10, 90)
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
