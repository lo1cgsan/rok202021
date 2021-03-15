/*
 * horner.cpp
 * 
 */

#include <iostream>
using namespace std;


void drukujw(int n, float tbwsp[]) {
	/*
	 * Funkcja drukuje postać wielomianu dla podanych
	 * danych wejściowych, np: 5*x^3 + 2*x^2 + 7*x^1 + 9
	 */
	 cout << "Wartość wielomianu o postaci:" << endl;

    int i = 0;
    for (i = 0; i < n; i++) {
        cout << tbwsp[i] << "x^" << n-i << " + ";
    }
    cout << tbwsp[i] << endl;
}

// W(x) = x (x (2x + 3) + 5) + 4
// W(1) = 2 + 3 + 5 + 4 = 14
float horner_it(int n, float tbwsp[], float x)
{
	// tbwsp = [2, 3, 5, 4]
	if (n == 0)
		return tbwsp[0];
	else
		return horner_it(n - 1, tbwsp, x) * x + tbwsp[n];
}


float horner_re(int n, float tbwsp[], float x)


int main(int argc, char **argv)
{
	int n = 0;  // stopień wielomianu
	float x = 0;
	cout << "Stopień: ";
	cin >> n;
	float tbwsp[n + 1];
	for (int i = 0; i <= n; i++) {
		cout << "Współczynnik przy potędze " << n - i << ": ";
		cin >> tbwsp[i];
	}
	cout << "Argument: ";
	cin >> x;
	
	drukujw(n, tbwsp);
	cout << "\ndla x = " << x << " wynosi: ";
	cout << horner_it(n, tbwsp, x) << endl;
	return 0;
}

