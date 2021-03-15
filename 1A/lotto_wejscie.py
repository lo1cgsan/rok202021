from random import randint

liczby = []  # pusta lista na losowane liczby
typy = []  # pusta lista na typy użytkownika

def losuj(ile, zakres):
    while ile > 0:
        liczba = randint(0, zakres)
        if liczba not in liczby:
            liczby.append(liczba)
            ile = ile - 1
        else:
            print("Powtórzenie...")


def pobierzTypy(ile):
    for i in range(ile):
        typ = int(input("Podaj swój typ: "))
        if typy.count(typ) == 0:
            typy.append(typ)
        else:
            print("Powtarzasz się!")


def main():
    ile = int(input("Ile liczb? "))
    zakres = int(input("Podaj zakres: "))

    losuj(ile, zakres)
    print()
    pobierzTypy(ile)
    print()
    print(liczby)
    print(typy)
    return 0

main()
