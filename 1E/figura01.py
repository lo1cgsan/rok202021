import turtle

def kwadrat():
    """
    Funkcja rysuje kwadrat
    o boku podanym przez użytkownika.
    """
    bok = int(input("Podaj bok: "))
    turtle.setup(800, 600)
    
    for i in range(4):
        turtle.forward(bok)
        turtle.left(90)

    turtle.done()
    

def figura():
    bok = int(input("Podaj bok: "))
    ile = int(input("Ile boków: "))
    kat = int(input("Podaj kąt: "))

    for i in range(ile):
        turtle.forward(bok)
        turtle.left(kat)


def uklad(szer, wys):
    turtle.setup(szer, wys)
    turtle.color("blue")
    turtle.width(3)
    turtle.goto(-szer // 2, 0)
    turtle.goto(szer // 2, 0)
    turtle.penup()
    turtle.goto(0, wys // 2)
    turtle.pendown()
    turtle.goto(0, -wys // 2)


def funkcja_liniowa():
    lx = list(range(-600, 620, 20))
    ly = []
    # f(n) = a * x + b
    for x in lx:
        ly.append(1 * x + 1)
    
    turtle.color("green")
    turtle.penup()
    turtle.goto(lx[0], ly[0])
    turtle.pendown()
    turtle.goto(lx[-1], ly[-1])
    

def main():
    szer = int(input("Podaj szerokość: "))
    wys = int(input("Podaj wyskość: "))
    uklad(szer, wys)
    funkcja_liniowa()
    turtle.done()
    
    return 0


main()
