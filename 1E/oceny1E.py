def main():
    for i in range(5):
        ocena = int(input("Podaj ocenę: "))
        if ocena > 0 and ocena < 7:
            print("Podałeś ocenę:", ocena)
        else:
            print("Błędne dane!")

    return 0


main()
