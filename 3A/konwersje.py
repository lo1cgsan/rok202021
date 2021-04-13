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
    lp = "221"
    for i in lp:
    
    return l


def main():
    liczba_p = input("Podaj liczbę wejściową: ")
    podst_p = int(input("Podaj podstawę systemu wejściowego: "))
    podst_k = int(input("Podaj podstawę systemu wyjściowego: "))

    print(l2dec(liczba_p, podst_p))
    
    return 0
    
    
main()
