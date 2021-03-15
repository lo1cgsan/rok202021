from random import randint


def losuj(ile, zakres):
    lista = []  # pusta lista
    for i in range(ile):
        liczba = randint(0, zakres)
        if lista.count(liczba) == 0:
            lista.append(liczba)
    return lista


def losuj2(ile, zakres):
    lista = []
    licznik = 0
    while ile > 0:
        licznik = licznik + 1
        liczba = randint(0, zakres)
        if liczba not in lista:
            lista.append(liczba)
            ile = ile - 1
        else:
            print("Powtórzenie")

    print(f"Liczba powtórzeń: {licznik}")

    return lista


def pobierzTypy(ile):
    lista = []
    while ile > 0:
        liczba = int(input("Podaj swój typ: "))
        if liczba not in lista:
            lista.append(liczba)
            ile = ile - 1
        else:
            print("Powtarzasz się!")
    return lista


def sprawdz(liczby, typy):
    trafione = 0
    for typ in typy:
        # if typ in liczby:
        for liczba in liczby:
            if typ == liczba:
                print(f"Trafiłeś: {typ}")
                trafione += 1
                break  # przerwanie pętli
    print(f"Trafiłeś {trafione} liczb!")


def main():
    ile = int(input("Ile liczb? "))
    zakres = int(input("Podaj zakres: "))

    liczby = losuj2(ile, zakres)
    typy = pobierzTypy(ile)
    sprawdz(liczby, typy)
    
    print(liczby)
    print(typy)
    return 0

main()
