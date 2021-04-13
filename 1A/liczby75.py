def main():

    suma = 0
    licznik = 0
    while suma <= 75:
        liczba = int(input("Podaj liczbę: "))
        licznik = licznik + 1
        suma = suma + liczba
    print(licznik)
    print(suma)
    return 0


main()
