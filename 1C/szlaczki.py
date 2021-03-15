#
##
###
####
#####
######
#######

def trojkat(znak, wys):
    for i in range(wys):
        for j in range(i + 1):
            print(znak, end='')
        print()


def main():
    znak = input("Podaj znak: ")
    wysokosc = int(input("Podaj wysokość: "))
    trojkat(znak, wysokosc)
    return 0
    
main()
