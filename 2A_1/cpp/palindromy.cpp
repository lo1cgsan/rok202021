/*
 * palindromy.cpp
 */

#include <iostream>
using namespace std;

int zlicz_znaki(char t[]) {
	int i = 0;
	while (t[i] != '\0') {
		i++;
	}
	return i;
}

bool czy_palindrom(char w[])
{
	int ile = zlicz_znaki(w);  // ilość znaków w wyrazie
	for (int i = 0; i < ile / 2; i++)
	{
		if (w[i] != w[ile - 1 - i])
			return false;
	}
	return true;
}

int main(int argc, char **argv)
{
	int r = 10;
	char wyraz[r];
	cout << "Podaj wyraz: " << endl;
	cin.getline(wyraz, r);
	if (czy_palindrom(wyraz))
		cout << "To palindrom!";
	else
		cout << "To nie jest palindrom.";
	return 0;
}

