/*
 * suma_liczb.cpp
 * 
 * Copyright 2020  <>
 * 
 * Program sumuje liczby z wygenerowanego zakresu
 *
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int suma = 0;  // definicja zmiennej
	int liczba = 0;  // zmienna iteracyjna (sterująca)
	
	int start = 0;
	int koniec = 0;
	cout << "Podaj początek zakresu: ";
	cin >> start;
	cout << "Podaj koniec zakresu: ";
	cin >> koniec;
	
	for (liczba = start; liczba < koniec + 1; liczba++) {
		cout << liczba << endl;
		suma = suma + liczba;
	}
	cout << "Suma: " << suma;
	return 0;
}

