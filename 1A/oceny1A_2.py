def main():
    
    liczba_ocen = int(input("Ile ocen? "))
   
    # while True:
    # while liczba_ocen > 0:
    for i in range(liczba_ocen):
        ocena = int(input("Podaj ocenę: "))

        # (-nieskończoność, 0>, <7, +nieskończoność)
        if ocena < 1 or ocena > 6:
            print("Błędne dane!")
        else:
            print("Podałeś ocenę:", ocena)

        # <1, 6>
        if ocena > 0 and ocena < 7:
            print("Podałeś ocenę:", ocena)
        else:
            print("Błędne dane!")

        liczba_ocen = liczba_ocen - 1

    return 0


main()
