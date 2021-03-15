/*
 * tablice_01.cpp
 * 
 * Program pobiera od użytkownika określoną przez niego liczbę ocen
 * i zapisuje je w tablicy. Następnie liczy ich średnią i drukuje wynik.
 * Pobieranie danych powinna realizować funkcja pobierz(), obliczanie średniej
 * – funkcja obliczSrednia(), drukowanie wyniku w funkcji głównej.
 * 
 */

#include <iostream>
using namespace std;

// funkcja, która nie zwraca wartości
void pobierz(int t[], int ile) {
	int ocena = 0;  // zmienna pomocnicza
	for (int i = 0; i < ile; i++) {
		cout << "Podaj ocenę: ";
		cin >> ocena;
		if (ocena > 0 && ocena < 7)
			t[i] = ocena;
		else {
			cout << "Błędne dane!" << endl;
			i--;
		}
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
	int oceny[ile];  // deklaracja tablicy
	
	pobierz(oceny, ile);
	
	cout << "Średnia ocen: " << obliczSrednia(oceny, ile) << endl;
	
	return 0;
}

