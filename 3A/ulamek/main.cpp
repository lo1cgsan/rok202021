#include <iostream>
#include "ulamek.h"

using namespace std;

int main(int argc, char **argv)
{
    Ulamek ul(4, 7);
    cout << "Twoj ulamek to: ";
    ul.wypisz();
    ul.set_lm(12, 6);
    cout << endl;
    ul.wypisz();
    cout << endl;
    Ulamek* wskUl = &ul;
    wskUl->wypisz();
	return 0;
}
