#include <iostream>
#include "ulamek.h"

using namespace std;

Ulamek::Ulamek(int l, int m) {
    licznik = l;
    if (!set_m(m)) exit(1);
}

bool Ulamek::set_lm(int l, int m) {
    licznik = l;
    return set_m(m);
}

bool Ulamek::set_l(int l) {
    licznik = l;
    return true;
}

bool Ulamek::set_m(int m) {
    if (m != 0) {
        mianownik = m;
        return true;
    } else {
        cout << "Mianownik nie może być zerem!" << endl;
    }
    return false;
}

void Ulamek::wypisz() {
    cout << licznik << "/" << mianownik;
}

int Ulamek::get_l() {
    return licznik;
}

int Ulamek::get_m() {
    return mianownik;
}

void Ulamek::skroc() {
    // NWD Euklidesa optymalny iteracyjny
    ;
}
