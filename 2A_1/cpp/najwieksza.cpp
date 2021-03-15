/*
 * najwieksza.cpp
 * 
 * Napisz program, który pobiera od użytkownika trzy liczby i drukuje
 * największą z nich.
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a = 0;  // deklaracja i inicjacja = definicja
	int b = 0;
	int c = 0;

	cout << "Podaj liczbę: ";
	cin >> a;

	cout << "Podaj liczbę: ";
	cin >> b;	

	cout << "Podaj liczbę: ";
	cin >> c;
	
	if (a > b && a > c) cout < a;
	else if (b > a && b > c) cout < b;
	else cout < c;
	
	return 0;
}

