liczby = [12, 11, 8, 6, 8, 4, 10, 5, 2, 3, 9, 100]

liczba = int(input("Podaj liczbę: "))

def wersja1():
    for i in range(len(liczby)):
        if liczba == liczby[i]:
            print("Znalazłem!")
            return
    print("Nie znalazłem!")


wersja1()

"""
Złożoność:
Lp_min = 1
Lp_max = n
O(n)
"""
