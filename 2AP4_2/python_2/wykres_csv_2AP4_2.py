import csv


def czytaj_csv(plik, separator=','):
    dane = []  # pusta lista
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for wiersz in tresc:
            dane.append(wiersz)
    return dane


def main ():
    dane = czytaj_csv("dane_klasa1A.csv", ";")
    dane.pop(0)  # usuń pierwszą listę
    nazwy_klas = [r[0] for r in dane]
    srednie = [float(r[1].replace(",", ".")) for r in dane]
    
    print(nazwy_klas)
    print(srednie)
    
    return 0
    
main()
