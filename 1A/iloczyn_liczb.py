def pobierzLiczby(ile):
    iloczyn = 1
    licznik = 0
    for i in range(ile):
        liczba = int(input("Podaj liczbę: "))
        if liczba > -1 and liczba < 21:
            if liczba % 2 == 0:
                print(liczba)
                iloczyn = iloczyn * liczba
                licznik = licznik + 1
                if iloczyn > 100:
                    break
        else:
            print("Błędne dane...")
    print("Iloczyn: ", iloczyn)
    print(f"Podano {licznik} liczb parzystych.")


def main():
    ile = int(input("Ile liczb? "))
    pobierzLiczby(ile)
    return 0


main()
