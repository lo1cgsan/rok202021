import csv
import numpy as np
import matplotlib.pyplot as plt


def czytaj_csv(nazwa_pliku, separator=","):
    dane = []
    with open(nazwa_pliku) as plik_csv:
        tresc = csv.reader(plik_csv, delimiter=separator)
        for wiersz in tresc:
            dane.append(wiersz)
    return dane


def main():
    dane = czytaj_csv("dane_klasa1A.csv", separator=";")
    dane.pop(0)
    ['1A', '5,35', '90%']
    
    nazwy_klas = [wiersz[0] for wiersz in dane]
    srednie = [float(wiersz[1].replace(',', '.')) for wiersz in dane]
    frekwencja = [float(wiersz[2].strip('%'))/100 for wiersz in dane]

    plt.bar(np.arange(len(nazwy_klas)), srednie)
    
    plt.twinx()
    plt.plot(frekwencja, "go")
    
    plt.show()
    
    return 0


main()
