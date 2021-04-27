import turtle


def kwadrat():
    for i in range(4):
        turtle.forward(120)
        turtle.right(90)


def figura(bok, ile, kat):
    for i in range(ile):
        turtle.forward(bok)
        turtle.right(kat)


turtle.setup(800, 600)
#for i in range(2, 102, 4):
#    figura(i)
# figura(120, 4, 90)
figura(120, 3, 120)

turtle.done()
