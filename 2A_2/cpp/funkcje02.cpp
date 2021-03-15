/*
 * funkcje02.cpp
 * 
 */

#include <iostream>
using namespace std;

int a = 0;  // zmienna globalna
int b = 0;

void sumuj(){
	int a = 5;
	int b = 5;
	int suma = a + b;
	cout << "Suma: " << suma;
}

int main(int argc, char **argv)
{
	cout << "Podaj liczby: " << endl;
	cin >> a;
	cin >> b;
	
	sumuj();  // wywołanie funkcji
	
	return 0;
}

