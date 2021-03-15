/*
 * anagramy.cpp
 * 
 */


#include <iostream>
using namespace std;

void anagramy(char w[], int r) {
	int i1, i2, i3, i4;
	for (i1 = 0; i1 < r; i1++) {
		for(i2 = 0; i2 < r; i2++) {
			if (i1 == i2) continue;
			for(i3 = 0; i3 < r; i3++) {
				if (i1 == i3 || i2 == i3) continue;
				// i4 = 6 - i1 + i2 + i3;
				for(i4 = 0; i4 < r; i4++) {
					if (i1 == i4 || i2 == i4 || i3 == i4) continue;
					cout << w[i1] << w[i2] << w[i3] << w[i4] << endl;
				}
			}
		}
	}
}


int main(int argc, char **argv)
{
	int r = 5;
	char wyraz[r];
	cin.getline(wyraz, r);
	cout << wyraz << endl;
	anagramy(wyraz, r-1);
	return 0;
}

