/*
 * czy_parzysta.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int liczba = 0;  // deklaracja i inicjacja zmiennej
	cout << "Podaj liczbę: ";
	cin >> liczba;

	if (liczba % 2 == 0) {
		cout << "liczba parzysta";
	} else {
		cout << "liczba nieparzysta";
	}
	
	return 0;
}

