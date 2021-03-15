/*
 * najwieksza.cpp
 * 
 * Napisz program, który pobiera od użytkownika 3 liczby
 * i drukuje największą.
 * 
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int najwieksza, liczba;
	najwieksza = liczba = 0;
	
	cout << "Podaj 1 liczbę: ";
	cin >> najwieksza;
	
	cout << "Podaj 2 liczbę: ";
	cin >> liczba;
	if (liczba > najwieksza) najwieksza = liczba;
	else if (liczba == najwieksza) cout << "liczby są równe" << endl;
	
	cout << "Podaj 3 liczbę: ";
	cin >> liczba;
	if (liczba > najwieksza) najwieksza = liczba;
	else if (liczba == najwieksza) cout << "liczby są równe" << endl;
	
	cout << "Największa: " << a << endl;
	return 0;
}

