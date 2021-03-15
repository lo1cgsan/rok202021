/*
 * T7_p8_1.cpp
 * 
 */


#include <iostream>
#include <cmath>
using namespace std;


int main(int argc, char **argv)
{
	float st, rad;
	st = 0.0;

	do {
		rad = st * M_PI/180;
		cout << "cos(" << st << ") = "
			 << cos(rad) << endl;
		st += 10.0;
	} while (st != 100);
	
	return 0;
}

