/*
 * funkcje01.cpp
 * 
 */


#include <iostream>

using namespace std;

void sumuj(int l1, int l2) {
	int suma = l1 + l2;
	cout << "Suma: " << suma << endl;
}

void odejmij(int l1, int l2) {
	int roznica = l1 - l2;
	cout << "Różnica: " << roznica << endl;
}

int pomnoz(int l1, int l2) {
	int iloczyn = l1 * l2;
	return iloczyn;
}

int main(int argc, char **argv)
{
	int liczba1, liczba2;
	cout << "Podaj liczby: ";
	cin >> liczba1;
	cin >> liczba2;
	
	// sumuj(liczba1, liczba2);
	// odejmij(liczba1, liczba2);
	
	cout << "Iloczyn: " << pomnoz(liczba1, liczba2) << endl;
	// int wynik = pomnoz(liczba1, liczba2);
	// cout << "Iloczyn: " << wynik << endl;
	
	return 0;
}

