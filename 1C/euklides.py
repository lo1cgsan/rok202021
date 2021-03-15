def nwd_v1(a, b):
    licznik = 0
    while a != b:
        licznik += 1
        if a > b:
            a = a - b
        else:
            b = b - a
    print("Powtórzeń:", licznik)
    print(a)


def nwd_v2(a, b):
    licznik = 0
    while a > 0:
        licznik += 1
        a = a % b
        b -= a
    print("Powtórzeń:", licznik)
    print(b)


def main():
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))
    nwd_v1(a, b)
    nwd_v2(a, b)
    return 0


main()
