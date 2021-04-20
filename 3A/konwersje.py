def l10_2x(l10, podst):
    reszty = []
    while l10 != 0:
        reszta = l10 % podst
        if reszta > 9:
            reszta = chr(reszta + 55)
        reszty.append(str(reszta))
        l10 = l10 // podst
    reszty.reverse()
    return ''.join(reszty)


def l2dec(lp, podst):
    if podst == 10:
        return lp
    l10 = 0
    lp = [ord(x) - 55 if 64 < ord(x) < 71 else int(x)
          for x in lp[::-1].upper()]
    for i, v in enumerate(lp):
        l10 += v * podst**i

    return l10


def l2dec_m(liczba_p, podst_p):
    if podst_p == 10:
        suma = liczba_p
        return suma

    elif podst_p <= 9:
        reszty = []
        licz = 0
        suma = 0
        liczba_p = str(liczba_p)
        x = len(liczba_p)
        for i in range(0, x):
            liczba_p[i]
            reszty.append(str(liczba_p[i]))
        reszty.reverse()
        for n in range(0, x):
            licz = int(reszty[n]) * (podst_p**n)
            suma = suma + licz
        return suma

    elif podst_p >= 11:
        reszty = []
        pomoc = []
        licz = 0
        suma = 0
        liczba_p = str(liczba_p)
        x = len(liczba_p)
        for i in range(0, x):
            if 65 <= ord(liczba_p[i]) <= 70:
                pomoc.append(ord(liczba_p[i]))
                reszty.append(str(int(pomoc[i]) - 55))
            elif 97 <= ord(liczba_p[i]) <= 102:
                pomoc.append(ord(liczba_p[i]))
                reszty.append(str(int(pomoc[i]) - 87))
            else:
                reszty.append(str(liczba_p[i]))
        reszty.reverse()
        for n in range(0, x):
            licz = int(reszty[n]) * (podst_p**n)
            suma = suma + licz
        return suma


def l2dec_b(lp, podst):
    l10 = 0
    lista_pom = []
    if podst == 10:
        return lp
    else:
        for i in lp:
            lista_pom.append(i)
        lista_pom.reverse()
        # lp[::-1]
        for i in range(0, len(lista_pom), 1):
            if ord(lista_pom[i]) > 64:
                l10 = l10 + (ord(lista_pom[i]) - 55)*podst**i
            else:
                l10 = l10 + (ord(lista_pom[i])-48)*podst**i
        return l10


def main():
    podst_p = int(input("Podaj podstawę systemu wejściowego: "))
    liczba_p = input("Podaj liczbę wejściową: ")
    podst_k = int(input("Podaj podstawę systemu wyjściowego: "))

    l10 = l2dec(liczba_p, podst_p)
    print(l10)
    print(l10_2x(l10, podst_k))

    return 0


main()
