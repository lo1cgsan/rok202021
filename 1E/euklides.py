def nwd_1(a, b):
    licznik = 0
    while a != b:
        licznik = licznik + 1
        if a > b:
            a = a - b
        else:
            b = b - a
    print(licznik)
    print(a)


def nwd_2(a, b):
    licznik = 0
    while a > 0:
        licznik = licznik + 1
        a = a % b
        b = b - a
        
    print(licznik)
    print(b)


def main():
    # pobranie danych wejściowych
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))
    nwd_1(a, b)
    print("=" * 20)
    nwd_2(a, b)
    return 0
    
    
main()
