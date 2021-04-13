def main():
    n = int(input("Podaj liczbę: "))
    m = int(input("Podaj liczbę: "))
    if n < m:
        for i in range(n, m + 1):
            print(i)
    else:
        print("Błędne dane!")
    return 0


main()
