/*
 * tablice_cw1.cpp
 */


#include <iostream>
using namespace std;

void drukuj(int t[], int ile) {
	for (int i = 0; i < ile; i++) {
		cout << "Indeks: " << i << " Wartość: " << t[i] << endl;
	}
}

void pobierzOceny(int t[], int ile) {
	int ocena = 0;  // zmienna pomocnicza
	for (int i = 0; i < ile; i++) {
		cout << "Podaj ocenę: ";
		cin >> ocena;
		if (ocena > 0 && ocena < 7)
			t[i] = ocena;
		else
			i--;
	}
}

float obliczSrednia(int t[], int ile) {
	int suma = 0;
	for (int i = 0; i < ile; i++) {
		suma += t[i];
	}
	return (float)suma / ile;
}

int main(int argc, char **argv)
{
	int ile = 0;
	cout << "Ile podasz ocen? ";
	cin >> ile;
	
	int oceny[ile];
	
	pobierzOceny(oceny, ile);
	drukuj(oceny, ile);
	
	cout << "Średnia: " << obliczSrednia(oceny, ile) << endl;
	
	return 0;
}

