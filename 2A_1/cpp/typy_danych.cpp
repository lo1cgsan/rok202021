/*
 * typy_danych.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int liczba = 0;
	cout << sizeof(liczba) << endl;
	// -2^31...2^31-1
	unsigned int liczba2 = 0;
	cout << sizeof(liczba2) << endl;
	// <0; 2^32-1>
	long int liczba3 = 0;
	cout << sizeof(liczba3) << endl;

	char znak = 'a';
	cout << sizeof(znak) << endl;
	cout << znak << endl;
	
	float liczba4 = 2.19;
	cout << sizeof(liczba4) << endl;

	double liczba5 = 2.191223354;
	cout << sizeof(liczba5) << endl;

	return 0;
}

