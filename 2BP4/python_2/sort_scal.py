d = [6, 5, 3, 1, 8, 7, 2, 4, 9]
i_p = 0
i_k = 8
i_s = 4
#    0  1  2                 n-1 
n = len(d)
p = [''] * n 

def MergeSort(i_p, i_k):
    i_s = (i_p + i_k + 1) // 2
    if i_s - i_p > 1:
        MergeSort(i_p, i_s - 1)
    if i_k - i_s > 0:
        MergeSort(i_s, i_k)
    
    i1 = i_p
    i2 = i_s
    for i in range(i_p, i_k + 1):
        if i1 == i_s or ((i2 <= i_k) and (d[i1] > d[i2])):
            p[i] = d[i2]
            i2 += 1
        else:
            p[i] = d[i1]
            i1 += 1


# p[i] = ((i1 == i_s) || ((i2 <= i_k) && (d[i1] > d[i2]))) ? d[i2++] : d[i1++];


def main()
    print(d)
    MergeSort(0, n - 1)
    print(d)
    return 0


main()
