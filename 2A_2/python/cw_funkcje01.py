def awans(lata, zarobek, staz):
    staz += 1
    zarobek = zarobek + 0.1 * zarobek
    return zarobek, staz

def drukuj(staz, zarobek):
    print("Po ", staz ," latach stażu bedziesz zarabiał: ", zarobek)

def main(args):
    staz = 1
    zarobek = 1000

    lata = int(input("Podaj przewidywaną ilość lat pracy: "))
    
    for i in range (lata-1):
        zarobek, staz = awans(lata, zarobek, staz)
        drukuj(staz, zarobek)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
