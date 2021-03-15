/*
 * funkcje01.cpp
 */


#include <iostream>
#include <cmath>
using namespace std;

void sumuj(int a, int b) {
	int suma = a + b;
    cout << "Suma: " << suma << endl;
}


int potega(int podstawa, int wykladnik) {
    int wynik = pow(podstawa, wykladnik);
    return wynik;
}

int main(int argc, char **argv)
{
	int liczba1 = 0;
	int liczba2 = 0;
	cout << "Podaj liczby: " << endl;
	cin >> liczba1;
	cin >> liczba2;

	sumuj(liczba1, liczba2);
	cout << potega(liczba1, liczba2) << endl;

	return 0;
}

