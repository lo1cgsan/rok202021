from random import randint


liczby = []  # definicja pustej listy, zmienna globalna
typy = []


def losuj(ile, zakres):
    for i in range(ile):
        liczba = randint(0, zakres)
        if liczba not in liczby:
            liczby.append(liczba)
        else:
            print("Liczba już wylosowana!")


def losuj2(ile, zakres):
    while ile > 0:
        liczba = randint(0, zakres)
        if liczba not in liczby:
            liczby.append(liczba)
            ile = ile - 1
        else:
            print("Liczba już wylosowana!")


def zgaduj(ile):
    # for i in range(ile):
    while ile > 0:
        typ = int(input("Podaj typ: "))
        if typ not in typy:
            #print("Trafiłeś!")
            typy.append(typ)
            ile = ile - 1
        else:
            print("Powtarzasz się!")

    # print(liczby)
    

def main():
    ile = int(input("Ile liczb wylosować? "))
    zakres = int(input("Podaj zakres? "))
    losuj2(ile, zakres)
    print(liczby)
    zgaduj(ile)
    print(typy)
    return 0


main()
