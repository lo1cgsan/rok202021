/*
 * wyszukiwanie_zlozonosc.cpp
 * 
 */


#include <iostream>
using namespace std;

int wyszukaj(int a[], int x, int n) {
	// złożoność O(n)
	int licznik = 0;
	for (int i = 0; i < n; i++) {
		licznik++;
		if (a[i] == x)
			return i;	
	}
	cout << "Elementów: " << n << endl;
	cout << "Porównań: " << licznik << endl;
	return -1;	
}


int main(int argc, char **argv)
{
	int x = 20;
	int n = 5;
	int a[n] = {4, 8, 34, 65, 1, 0, 8, 3, 7, 1};
	cout << wyszukaj(a, x, n) << endl;

	return 0;
}

