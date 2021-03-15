
def srednia(oceny):
	print("Średnia wynosi: ", sum(oceny) / len(oceny))


def mediana(oceny):
	oceny = sorted(oceny)  # sortowanie rosnące listy
	ile = len(oceny)
	if ile % 2 == 0:
		indeks = int(ile / 2)
		mediana = (oceny[indeks] + oceny[indeks-1]) / 2
	else:
		mediana = oceny[int(ile / 2)]
	
	print("Mediana wynosi:", mediana)



def main(args):
	ile = 20
	oceny = []
	ocenyile = [0, 0, 0, 0, 0, 0, 0]
	while ile > 0:
		ocena = int(input("Podaj ocenę lub zero, aby zakończyć: "))
		if ocena > 0 and ocena < 7:
			oceny.append(ocena)
			ocenyile[ocena] += 1
			ile -= 1
		elif ocena == 0:
			break;
		else:
			print("Wprowadzono niepoprawną ocenę")

	for i in range(1,7):
		print(f"Ocen {i}: {ocenyile[i]}")
	srednia(oceny)
	mediana(oceny)

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
