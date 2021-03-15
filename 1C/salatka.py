
def main():
    skladnik = int(input("Podaj ilość składnika (g): "))
    ilosc_porcji = int(input("Podaj ilość osób na porcję: "))
    ilosc_gosci = int(input("Podaj ilość gosci: "))
    potrzebna_ilosc = (skladnik * ilosc_gosci) / ilosc_porcji
    # print ("Dla", ilosc_gosci, "osób potrzeba", potrzebna_ilosc, "składnika sałatki")
    print (f"Dla {ilosc_gosci} osób potrzeba {potrzebna_ilosc} składnika sałatki")
    return 0


main()
