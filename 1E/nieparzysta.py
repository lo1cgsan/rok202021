# Program szuka nieparzystej liczby w wylosowanej liście liczb.
# Napisz funkcję szukaj(), która sprawdzi,
# czy w liście jest jakaś nieparzysta liczba.
# Jeżeli tak, funkcja powinna natychmiast przerwać działanie
# i wydrukować komunikat "Znaleziono liczbę {liczba}.".
# Jeżeli nie, wydrukuj komunikat "Nie znaleziono."

from random import randint


def losuj(ile, liczby):
    for i in range(ile):
        liczby.append(randint(0, 100))


def szukaj_nieparzystej(liczby):
    """
    Funkcja szuka nieparzystej liczby
    w przekazanej liście liczb.
    """
    for liczba in liczby:
        if liczba % 2 == 1:
            print("Znalazłem:", liczba)
            break


def main():
    liczby = []
    ile = int(input("Ile liczb wylosować? "))
    losuj(ile, liczby)
    print(liczby)
    szukaj_nieparzystej(liczby)


main()
