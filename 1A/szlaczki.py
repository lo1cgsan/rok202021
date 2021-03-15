def rysujT(znak):
    ile = int(input("Podaj wysokość: "))
    for i in range(ile):
        for j in range(i + 1):
            print(znak, end="")
        print()


def main():
    znak = input("Podaj znak: ")
    rysujTrojkat(znak)
    return 0


main()
