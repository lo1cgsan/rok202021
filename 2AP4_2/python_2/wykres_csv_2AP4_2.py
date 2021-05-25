import csv
import numpy as np
import matplotlib.pyplot as plt


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
    print()
    ile = np.arange(len(nazwy_klas))
    print(ile)
    print()
    plt.title("Średnie klas")
    plt.bar(ile, srednie)
    plt.ylim([0.1, 6.0])
    plt.xticks(ile, nazwy_klas)
    
    frek = [float(r[2].strip("%")) / 100 for r in dane]
    print(frek)

    plt.twinx()
    plt.plot(frek, color="red")
    wartosci = plt.yticks()
    plt.ylabel(['{(x * 100):2.0f}%' for z in wartosci])
    plt.show()
    return 0

    
main()
