/*
 * dodaj_liczby.cpp
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv) {
	// int liczba1;  // deklaracja zmiennej całkowitej
	// int liczba2;
	float liczba1;
	float liczba2;
	liczba1 = 0;  // inicjacja zmiennej
	liczba2 = 0;
	cout << "Podaj dwie liczby całkowite: ";
	cin >> liczba1;
	cin >> liczba2;
	cout << liczba1 << " " << liczba2 << endl;
	cout << "Suma: " << liczba1 + liczba2;
	return 0;
}

