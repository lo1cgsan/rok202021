def dec2bin(l):
    lbin = []
    while l != 0:
        lbin.append(l % 2)
        l //= 2
    lbin.reverse()
    return lbin


def poteguj2(x, k):
    k = dec2bin(k)
    print(k)
    k.reverse()
    p = x
    for i in range(len(k) - 2, -1, -1):
        if k[i] == 1:
            p = p * p * x
        else:
            p = p * p
    return p


def main():
    k = int(input("Podaj wykładnik:"))
    x = float(input("Podaj podstawę:"))
    print(poteguj2(x, k))
    return 0


main()
