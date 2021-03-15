from random import randint

liczby = []  # pusta lista
typy = []

def losuj(ile, zakres):
    for i in range(ile):
        liczba = randint(0, zakres)
        if liczba not in liczby:
            liczby.append(liczba)
        else:
            print("Nie dodano liczby!")


def losuj2(ile, zakres):
    while ile > 0:
        liczba = randint(0, zakres)
        if liczba not in liczby:
            liczby.append(liczba)
            ile = ile - 1
        else:
            print("Nie dodano liczby!")


def zgaduj():
    for i in range(3):
        typ = int(input("Podaj typ: "))
        if typ in liczby:
            print("Zgadłeś!")
        else:
            print("Pudło...")


def zgaduj2(ile):
    while ile > 0:
        typ = int(input("Podaj typ: "))
        if typ not in typy:
            typy.append(typ)
            ile = ile - 1
        else:
            print("Ta liczba już wystąpiła...")


def main():
    ile = int(input("Ile liczb wylosować? "))
    zakres = int(input("Podaj zakres: "))
    losuj2(ile, zakres)
    zgaduj2(ile)
    print(liczby)
    print(typy)
    return 0

main()
