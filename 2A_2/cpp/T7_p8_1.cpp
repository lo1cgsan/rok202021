/*
 * T7_p8_1.cpp
 * 
 */
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
	float st = 0.0;
	float rad = 0;
	do {
		rad = st * M_PI / 180;
		cout << "cos(" << st << ") = "
		     << cos(rad) << endl;
		st += 10.0;
		// if (st > 90) break;
	} while (cos(rad) != 0);
	return 0;
}

