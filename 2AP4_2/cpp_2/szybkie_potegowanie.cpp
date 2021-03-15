/*
 * szybkie_potegowanie.cpp
 */
#include <iostream>
using namespace std;

int dec2bin(int k, int t[])
{
	
	int i = 0;
	while(k != 0)
	{
		t[i] = k % 2;
		k = k / 2;
		i++;
	}
	return i;
	
}

float poteguj_szybko(int x, int k){
	int roz = 8;
	float p = x;
	int k2tab[roz];
	int n = dec2bin(k, k2tab);
	// for(int i = 0; i < roz; i++)
	//	cout << k2tab[i] << " ";
	for(int i = n - 2; i >= 0; i--)
		if (k2tab[i] == 1)
			p = p * p * x;
		else
			p = p * p;
			
	return p;
}


int main(int argc, char **argv)
{
	int k;
	float x;
	cout << "Podaj wykładnik: ";
	cin >> k;
	cout << "Podaj podstawę: ";
	cin >> x;
	cout << poteguj_szybko(x, k);
	return 0;
}

