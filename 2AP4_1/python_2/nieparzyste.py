# 1. pobierz wartość liczby n.
# 2. 
def wersja1(n):
    for i in range(1, n + 1, 2):
        print(i)

def wersja2(n):
    i = 1
    # while i <= n:
    while i < n + 1:
        print(i)
        i += 2

n = int(input("Podaj liczbę: "))
wersja2(n)

192.168.3.3:8000
