#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja1.py
import turtle

def rysuj_it(ile, dlboku, kat):
    for i in range(ile):
        turtle.forward(dlboku)
        turtle.right(kat)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)

def rysuj_rek(ile, dlboku, kat):
    print(ile)
    if ile < 1:
        return
    turtle.forward(dlboku)
    turtle.right(kat)
    
    rysuj_rek(ile - 1, dlboku, kat)
    

def main(args):
    turtle.setup(800, 600)
    # rysuj_it(4, 100, 90)
    rysuj_rek(4, 100, 90)
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
