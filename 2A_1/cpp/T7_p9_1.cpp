/*
 * T7_p9_1.cpp
 * Wyszukiwanie liczby w tablicy
 */

#include <iostream>
using namespace std;

int szukaj(int tab[], int n, int x) {
	int i;
	for(i = 0; i < n; i++)
		if (tab[i] == x)
			return i;
	cout << "Powtórzeń: " << i << endl;
	return -1;
}


int main(int argc, char **argv)
{
	int n = 5 + 1;
	int x = 10;
	int tab[] = {3, 6, 1, 8, 9, 12};
	cout << szukaj(tab, n, x);
	return 0;
}

