from osoba import Osoba

def main():
    osoba1 = Osoba()
    osoba1.set_Imie('Anna')
    print(osoba1.get_Imie())
    
    print(osoba1.__dict__)
    return 0

main()
