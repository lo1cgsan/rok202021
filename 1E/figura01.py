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

    turtle.setup(800, 600)
    for i in range(ile):
        turtle.forward(bok)
        turtle.left(kat)

    turtle.done()


def main():
    figura()
    return 0


main()
