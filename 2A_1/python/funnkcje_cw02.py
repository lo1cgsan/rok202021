def srednia(oceny):
   return sum(oceny) / len(oceny)


def mediana(oceny):
    oceny = sorted(oceny)
    if  len(oceny) % 2 == 0:
        polowa = int(len(oceny) / 2)
        return sum(oceny[polowa - 1:polowa + 1]) / 2
    else:
        return oceny[int(len(oceny) / 2)]

def oceny(c):
    for i in c:
        licznik = c.count(i)
        print("Ocena", i, "występuje", licznik, "razy")
    return 0


def main(args):
    ile = 20
    oceny = []  # lista ocen
    ocena = 0
    print("Podanie oceny 0 przerywa pobieranie ocen.")
    while ile > 0:
        ocena = int(input("Podaj oceny: "))
        if ocena > 0 and ocena < 7:
            oceny.append(ocena)
            ile -= 1
        elif ocena == 0:
            break
        else:
            print("Błędne dane!")

    print(f"Podano {len(oceny)} ocen.")
    print("Średnia wynosi", srednia(oceny))
    print("Mediana wynosi:", mediana(oceny)) 

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
