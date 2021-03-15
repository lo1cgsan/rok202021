/*
 * czy_parzysta.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a;
	a = 0;
	cout << "Podaj liczbę: ";
	cin >> a;

	if (a % 2 == 0) {
		cout << "parzysta";
	} else {
		cout << "nie parzysta";
	}
	
	return 0;
}

