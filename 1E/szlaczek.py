# szlaczek.py

#
##
###
####
#####
######

def rysuj_trojkat(znak, wys):
    for i in range(wys):
        for j in range(i + 1):
            print(znak, end="")
        print()


def main():
    znak = input("Podaj znak: ")
    wys = int(input("Wysokość: "))
    rysuj_trojkat(znak, wys)
    
    return 0


main()
