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
    frekwencje = [float(wiersz[2].strip('%'))/100 for wiersz in dane]

    wsp_x = np.arange(len(srednie))
    plt.bar(wsp_x, srednie)
    
    plt.twinx()
    plt.plot(frekwencje, "go")
    
    plt.show()
    return 0


main()
