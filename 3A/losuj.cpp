/*
 * losuj.cpp
 * 
 */


#include <iostream>
using namespace std;

void losuj1(int t[], int r, int a, int b) {
	long long int tmp = 1;
	for (int i = 0; i < 1000000000; i++) {
		tmp = tmp * i;
		if (tmp > 1000000) tmp = tmp % i;
	}
	long int czas = time(NULL);
	cout << "Czas: " << czas << endl;
	srand(czas);
	
	for (int i = 0; i < r; i++) {
		// zakres <0; r>
		// t[i] = rand() % (r + 1);
		// zakres <a; b>
		t[i] = a + rand() % (b - a + 1);
		
	}
}

void drukuj(int t[], int r) {
	for (int i = 0; i < r; i++) {
		cout << t[i] << " ";
	}
	cout << endl;
}


void losuj3(float t[], int r) {
	int a = 5;
	int b = 20;
	srand(time(NULL));
	for (int i = 0; i < r; i++) {
		t[i] = ((float)rand()/RAND_MAX) * (b - a);
	}
}

void drukuj3(float t[], int r) {
	for (int i = 0; i < r; i++) {
		cout << t[i] << " ";
	}
	cout << endl;
}


int main(int argc, char **argv)
{
	cout << time(NULL);
	cout << "Ile liczb wylosować? ";
	int ile = 0;
	cin >> ile;
	int tab[ile];
	for (int i=0; i < 5; i++) {
		losuj1(tab, ile, 5, 20);
		drukuj(tab, ile);
	}
	float tab2[ile];
	losuj3(tab2, ile);
	drukuj3(tab2, ile);
	return 0;
}

