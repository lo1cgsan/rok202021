ciag_a = [1, 3, 4, 6, 9]
ciag_b = [2, 5, 7, 8, 10]
wynik = []


def scal():
    global wynik
    ile1 = len(ciag_a)
    ile2 = len(ciag_b)
    i1 = 0
    i2 = 0
    for i in range(len(ciag_a) * 2):
        # print(ciag_a[i1], ciag_b[i2])
        if ile1 > 0 and ile2 > 0:
            if ciag_a[i1] < ciag_b[i2]:
                wynik.append(ciag_a[i1])
                i1 += 1
                ile1 -= 1
            else:
                wynik.append(ciag_b[i2])
                i2 += 1
                ile2 -= 1
        # print(i1, i2)
        # print(ile1, ile2)
        # print()

    if ile1:
        wynik += ciag_a[i1:]
    elif ile2:
        wynik += ciag_b[i2:]
    print(wynik)


def main():
    scal()
    return 0


main()
