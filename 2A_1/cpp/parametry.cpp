/*
 * parametry.cpp
 */


#include <iostream>
using namespace std;

void zwieksz(int a) {
	a += 2;  // zwiększenie wartości o 2, tj. a = a + 2
	cout << a << endl;
}

void zwieksz2(int &a) {  // przekazanie parametru przez referencję
	a += 2;  // zwiększenie wartości o 2, tj. a = a + 2
	cout << a << endl;
}


void zwieksz3(int b[]) {  // przekazanie parametru przez referencję
	b[0] = b[0] + 2;
	cout << b[0] << endl;
}


int main(int argc, char **argv)
{
	int a = 5;
	cout << a << endl;
	zwieksz(a);
	cout << a << endl;

	zwieksz2(a);
	cout << a << endl;
	
	int b[1] = {5};  // deklaracja i inicjacja 1-elementowej tablicy
	cout << b[0] << endl;
	zwieksz3(b);
	cout << b[0] << endl;
	
	cout << b << endl;

	return 0;
}

