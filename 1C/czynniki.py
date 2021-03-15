
def rozloz(liczba):
    k = 2
    while liczba > 1:
        while liczba % k == 0:
            print(k)
            liczba = liczba / k
        k = k + 1


def main():
    liczba = int(input("Podaj liczbę: "))
    rozloz(liczba)
    return 0


main()
