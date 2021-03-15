/*
 * tablice_01.cpp
 * 
 */
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int ile = 0;
	cout << "Ile podasz ocen? ";
	cin >> ile;
	int oceny[ile];
	
	for (int i = 0; i < ile; i++) {
		cout << "Podaj ocenę: ";
		cin >> oceny[i];
	}
	
	cout << endl;
	
	for (int i = 0; i < ile; i++) {
		cout << i << " => " << oceny[i] << endl;
	}

	return 0;
}

