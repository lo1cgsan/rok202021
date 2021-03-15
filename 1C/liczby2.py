# liczby2.py

def drukuj_liczby():
    for i in range(1, 10):
        for j in range(10):
            if i != j:
                print(f"{i}{j}")


def main():
    drukuj_liczby()
    return 0


main()
