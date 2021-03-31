def main():
    suma = 0
    # for i in range(5):
    while suma <= 75:
        liczba = int(input("Podaj liczbę: "))
        suma = suma + liczba
        print(liczba, suma)

    print("Suma:", suma)
    return 0
    

main()
