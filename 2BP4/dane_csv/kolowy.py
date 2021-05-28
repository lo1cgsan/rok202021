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
    dane = czytaj_csv('dane_wybory.csv',';')
    
    etykiety = [wiersz[0] for wiersz in dane]
    glosy = [int(wiersz[1]) for wiersz in dane]
    
    plt.pie(glosy, [0.1, 0, 0, 0.05], etykiety)
    
    plt.show()
    return 0


main()
