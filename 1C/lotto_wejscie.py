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


def pobierzTypy(ile=5):
    for i in range(ile):
        typ = int(input("Podaj swój typ: "))
        if typy.count(typ) == 0:
            typy.append(typ)
        else:
            print("Powtarzasz się!")


def sprawdz():
    trafione = 0
    for typ in typy:
        if liczby.count(typ) > 0:
            trafione = trafione + 1
    print(f"Zgadłeś {trafione} liczb!")


def main():
    ile = int(input("Ile liczb? "))
    zakres = int(input("Podaj zakres: "))

    losuj(ile, zakres)
    print()
    pobierzTypy(ile)
    print()
    sprawdz()
    print(liczby)
    print(typy)
    return 0

main()
