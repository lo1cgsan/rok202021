/*
 * potega.cpp
 */


#include <iostream>
using namespace std;

int potega_it(int p, int w) {
	int wynik = 1;
	for (int i = 0; i < w; i++) {
		wynik = wynik * p;
	}
	return wynik;
}

int main(int argc, char **argv)
{
	int podstawa = 0;
	int wykladnik = 0;
	cout << "Podaj podstawę i wykladnik:" << endl;
	cin >> podstawa;
	cin >> wykladnik;
	cout << "Wynik: " << potega_it(podstawa, wykladnik);
	return 0;
}

