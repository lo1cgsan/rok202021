tablica = [12, 11, 8, 6, 8, 4, 10, 5, 2, 3, 0]

liczba = int(input("Podaj liczbę: "))

def wersja1():
    for i in range(len(tablica)):
        if liczba == tablica[i]:
            print("Znalazłem")
            return
    print("Nie znalazłem")


wersja1()

"""
Skrajne przypadki:
n = 12
Lp = 1, n
O(n) => złożoność liniowa
O(n^2)
O(n!)
"""

