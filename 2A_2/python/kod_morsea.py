kod = ['*-', '-***', '-*-*', '-**', '*', '**-*']


def koduj(tekst):
    for znak in tekst:
        if znak != " ":
            print(kod[ord(znak.lower()) - 97] + "/", end="")
        else:
            print("/")
        

def dekoduj(komunikat):
    # *-/-***/-**//
    # .split()
    pass


def main():
    tekst = input("Podaj tekst: ")
    koduj(tekst)
    return 0


main()
