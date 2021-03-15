/*
 * teksty_01.cpp
 */


#include <iostream>
using namespace std;

void pobierz1(char t[]) {
	cin >> t;
}

void pobierz2(char t[], int r) {
	cin.getline(t, r);
}

void drukuj1(char t[], int ile) {
	for (int i = 0; i < ile; i++) {
//		if (t[i] == '\0') break;
		cout << "Indeks: " << i << " Wartość: " << t[i] << endl;
	}
}

void drukuj2(char t[]) {
	int i = 0;
	while (t[i] != '\0') {
		cout << "Indeks: " << i << " Wartość: " << t[i] << endl;
		i++;
	}
}

int zlicz_znaki(char t[]) {
	int i = 0;
	while (t[i] != '\0') {
		i++;
	}
	return i;
}

int main(int argc, char **argv)
{
	char znak = 'a';
	cout << (int)znak << endl;
	
	int kod = 65;
	cout << (char)kod << endl;

	int rozmiar = 10;
	char znaki[rozmiar];  // deklaracja tablicy
	// pobierz1(znaki);
	// drukuj1(znaki, rozmiar);
	// cout << endl;
	pobierz2(znaki, rozmiar);
	drukuj2(znaki);
	cout << "Wprowadzono " << zlicz_znaki(znaki) << " znaków." << endl;
	return 0;
}

