# silnia


def silnia_it(n):
    wynik = 1
    # for(i = 2; i <= n; i++)
    for i in range(2, n + 1):
        wynik = wynik * i
    return wynik


# n! = 1 dla n = 0
# n! = n * (n - 1)!
# ~4! = 4 * 3! // zapamiętane w 0x10
# ~3! = 3 * 2! // zapamiętane w 0x12
# ~2! = 2 * 1! // zapamiętane w 0x14
# ~1! = 1 * 0! // zapamiętane w 0x16
# ~1! = 1 * 1
# ~2! = 2 * 1
# ~3! = 3 * 2
# ~4! = 4 * 6

def silnia_rek(n):
    if n == 0:
        return 1
    return n * silnia_rek(n - 1)


def main(args):
    n = int(input("Podaj liczbę: "))
    print(f"{n}! = {silnia_it(n)}")
    # print(f"{n}! = {silnia_rek(n)}")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
