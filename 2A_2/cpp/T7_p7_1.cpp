/*
 * T7_p7_1.cpp
 * 
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int n = 0;
	cout << "Podaj liczbę: ";
	cin >> n;
	int i = 1;
	while (1) {
		if (i == n) break;
		cout << i << endl;
		i += 2;		
	};
	
	return 0;
}

