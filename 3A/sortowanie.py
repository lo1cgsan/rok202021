
def sort_bubble(lista, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                # tmp = lista[j]
                # lista[j] = lista[j + 1]
                # lista[j + 1] = tmp
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def sort_insert(lista, n):
    for i in range(1, n):
        el = lista[i]
        j = i - 1
        while j > -1 and lista[j] > el:
            lista[j + 1] = lista[j]
            j = j - 1
        pass


def main():
    lista = [6, 5, 3, 1, 8, 7, 2, 4]
    n = len(lista)
    # lista = sort_bubble(lista, n)
    lista = sort_insert(lista, n)
    print(lista)
    return 0


main()
