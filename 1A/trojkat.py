def czyTrojkat(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        print("Da się")
    else:
        print("Nie da się")

def main():
    a = int(input("Podaj 1. bok: "))
    b = int(input("Podaj 2. bok: "))
    c = int(input("Podaj 3. bok: "))
    czyTrojkat(a, b, c)
    return 0

main()