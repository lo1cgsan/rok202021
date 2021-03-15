/*
 * trojkat.cpp
 * 
 * Napisz program, który sprawdza, czy z trzech boków podanych
 * przez użytkownika, można zbudować trójkąt.
 * Na końcu wyprowadź odpowiedni komunikat, np. "da się"
 * lub "nie da się".
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a, b, c;
	a = b = c = 0;
	cout << "Podaj bok 1: ";
	cin >> a;
	cout << "Podaj bok 2: ";
	cin >> b;
	cout << "Podaj bok 3: ";
	cin >> c;
/*	
	if (a + b > c) {
		if (a + c > b) {
			if (b + c > a) {
				cout << "da się";
				// return 0;
			} else {
				cout << "nie da się";
			}
		} else {
			cout << "nie da się";
		}
	} else {
		cout << "nie da się";
	}
	
	// cout << "nie da się";
*/
	
	if (a + b > c && a + c > b && b + c > a) {
		cout << "da się";
	} else {
		cout << "nie da się";
	}
	
	return 0;
}

