def pobierzliczby(lista, ile):
	for i in range(ile):
		liczba1 = int(input("Podaj liczbe: "))
		lista.append(liczba1)


def sumuj(lista):
	suma = 0
	for liczba in lista:
		suma += liczba
	return suma
			

def main(args):
	ile = 5  # ilość liczb w listach
	lista1 = [] 
	lista2 = []
	pobierzliczby(lista1, ile)
	print("Teraz druga seria liczb!")
	pobierzliczby(lista2, ile)
	print(lista1)
	print(lista2)
	suma1 = sumuj(lista1)
	suma2 = sumuj(lista2)
	print("Suma w tablicy pierwszej: ", suma1)
	print("Suma w tablicy drugiej: ", suma2)
	if suma1 > suma2:
		print("Lista pierwsza jest większa od listy drugiej")
	else:
		print("Lista druga jest większa od listy pierwszej")

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
