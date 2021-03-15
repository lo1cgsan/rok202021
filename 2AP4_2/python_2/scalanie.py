ciag_a = [1, 3, 4, 6, 9]
ciag_b = [2, 4, 5, 7, 8, 10, 12]
ciag_ab = []


def scal():
    ile1 = len(ciag_a)
    ile2 = len(ciag_b)
    i1 = 0
    i2 = 0
    # czy pętlę for da się zastąpić pętlą while?
    for i in range(ile1 * 2):
        if i1 < ile1 and i2 < ile2:
            if ciag_a[i1] < ciag_b[i2]:
                ciag_ab.append(ciag_a[i1])
                i1 += 1
            else:
                ciag_ab.append(ciag_b[i2])
                i2 += 1
    # w której liście pozostały liczby?
    # dopisz pozostałe liczby do ciągu wynikowego
    
    print(ciag_ab)


scal()
