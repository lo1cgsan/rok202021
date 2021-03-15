#include <iostream>

using namespace std;

int main()
{
	int n;
    cout << "podaj liczbe: ";
    cin >> n;
    int i = 1;
    while (1) {
        if (i == n) break;
        cout << i << " ";
        i = i + 2;
    }
}
