/*
 * funkcje02.cpp
 * 
 */


#include <iostream>

using namespace std;

int liczba1 = 0;
int liczba2 = 0;  // zmienne globalne

void sumuj() {
	int suma = liczba1 + liczba2;
	cout << "Suma: " << suma << endl;
}

int main(int argc, char **argv)
{
	// int liczba1, liczba2;  // zmienne lokalne
	cout << "Podaj liczby: ";
	cin >> liczba1;
	cin >> liczba2;
	cout << "Suma: " << liczba1 + liczba2 << endl;
	
	sumuj();
	
	return 0;
}

