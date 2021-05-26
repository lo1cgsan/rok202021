import csv
import numpy as np
import matplotlib.pyplot as plt


def czytaj_csv(nazwa_pliku, separator=','):
    dane = []
    with open(nazwa_pliku, newline='', encoding='utf-8') as plik_csv:
        tresc = csv.reader(plik_csv, delimiter=separator)
        for wiersz in tresc:
            dane.append(wiersz)
    return dane


def main():
    dane = czytaj_csv('dane_klasa1A.csv',';')
    print(dane.pop(0))
    #print(dane)
    
    nazwy_klas = [wiersz[0] for wiersz in dane]
    srednie = [float(wiersz[1].replace(',', '.')) for wiersz in dane]
    frekwencje = [wiersz[2] for wiersz in dane]

    print(srednie)
    
    plt.plot(srednie)
    plt.show()
    return 0


main()
