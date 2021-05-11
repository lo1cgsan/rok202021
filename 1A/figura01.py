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


def funkcja(x):
    a = 1
    b = 1
    return a * x + b


def wykres_funkcji():
    lx = list(range(-300, 300, 50))
    ly = []
    for x in lx:
        ly.append(funkcja(x))
    print(lx)
    print(ly)
    
    for i in range(len(lx) - 1):
        rysujLinie(lx[i], ly[i], lx[i+1], ly[i+1])
    

szer = 800
wys = 600

turtle.setup(szer, wys)
rysujLinie(-szer / 2, 0, szer / 2, 0)
rysujLinie(0, -wys / 2, 0, wys / 2)
wykres_funkcji()
#figura(100, 4, 90)
#figura(120, 3, 120)
turtle.done()
