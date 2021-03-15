/*
 * typy.cpp
 * 
 */

#include <iostream>
#include <fstream>
using namespace std;

// definicja stałej
#define ROZMIAR 20

enum REZULTAT
{
	ISTNIEJE = 1,
	NIEISTNIEJE = -1
};

REZULTAT czyjest(const char *npliku)
{
	ifstream f(npliku);
	if (f.good()) {
		f.close();
		return ISTNIEJE;
	} else {
		f.close();
		return NIEISTNIEJE;
	}
}

void typwylicz() {
	// użycie typu stałej ROZMIAR i typu wyliczeniowego
	char plik[ROZMIAR];
	cout << plik << endl;
	cout << "Podaj nazwę pliku: ";
	cin.getline(plik, ROZMIAR);
	cout << "Nazwa: " << plik << endl;
	
	REZULTAT jestplik;
	jestplik = czyjest(plik);
	if (jestplik == ISTNIEJE)
		cout << "Jest plik!";
	else
		cout << "Nie ma pliku!";
}

void nowytyp()
{
	// użycie typedef
	typedef string str;
	str x;
	cout << "Podaj tekst: ";
	cin >> ws >> x;
	cout << x << endl;
}

int main(int argc, char **argv)
{
	// nowytyp();
	typwylicz();
	return 0;
}

