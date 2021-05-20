def aukcje():
    liczba_sztuk = int(input("Ile sztuk? "))
    cena = float(input("Jaka cena? "))
    if liczba_sztuk * cena < 20:
        print("12,50 zł")
    else:
        print("9,90 zł")    


def telefony():
    forma_doladowania = input("Jak doładujesz konto? ")
    if forma_doladowania == "internet":
        print("Bonus: 10%")


def main():
    aukcje()
    telefony()
    return 0


main()
