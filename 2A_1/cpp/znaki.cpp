/*
 * znaki.cpp
 * 
 */
#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
	char znak;
	znak = 'a';
	cout << znak << endl;
	cout << (int)znak << endl;

	int kod = 65;
	int kod2 = 8;
	cout << (char)kod << (char)kod2 << endl;

	for (int i=0; i < 128; i++)
		cout << (char)i << endl;

	return 0;
}

