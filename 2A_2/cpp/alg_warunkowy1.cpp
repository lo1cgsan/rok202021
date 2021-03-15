/*
 * alg_warunkowy1.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int w = 0;  // deklaracja i inicjacja => definicja zmiennej
	cout << "Podaj wynik testu: ";
	cin >> w;
	
	if (w < 0 || w > 60) {
		cout << "Błędne dane!";
		return 0;
	}
	
	// instrukcja warunkowa złożona
	if (w < 20) cout << "podstawowa";
	else if (w <= 40) cout << "średniozaawansowana";
	else cout << "zaawansowana";
	
	return 0;
}

