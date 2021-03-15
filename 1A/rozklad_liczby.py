
def rozloz(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n = n // k
            czynniki.append(k)
        k += 1
    return czynniki


def main():
    n = int(input("Podaj liczbę: "))
    print(rozloz(n))
    return 0
    
    
main()
