import turtle

def kwadrat():
    # sekwencja: [0, 1, 2, 3], "abcd"
    for i in "abcd":
        turtle.forward(150)
        turtle.right(90)


def rysujLinie(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()


def figura(bok, ile_b, kat):
    for i in range(ile_b):
        turtle.forward(bok)
        turtle.right(kat)


szer = 800
wys = 600

turtle.setup(900, 500)

rysujLinie(-400, 0, 400, 0)
rysujLinie(0, -300, 0, 300)
#figura(100, 4, 90)
#figura(120, 3, 120)
turtle.done()
