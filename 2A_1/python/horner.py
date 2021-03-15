def drukujw(n, tbwsp):
    # Funkcja drukuje postać wielomianu dla podanych
    # danych wejściowych, np: 5*x^3 + 2*x^2 + 7*x^1 + 9
    
    print("Wartość wielomianu o postaci:")

    for i in range(n + 1):
        cout << tbwsp[i] << "x^" << n-i << " + ";
    cout << tbwsp[i] << endl;


// W(x) = x (x (2x + 3) + 5) + 4
// W(1) = 2 + 3 + 5 + 4 = 14
float horner_it(int n, float tbwsp[], float x)
{
    // tbwsp = [2, 3, 5, 4]
    float wynik = tbwsp[0];
    for (int i = 1; i < n + 1; i++)
    {
        wynik = wynik * x + tbwsp[i];
        cout << wynik << endl;
    }
    return wynik;
}



def main():
    n = int(input("Stopień: "))  // stopień wielomianu
    tbwsp = []  // lista współczynników
    for i in range(n + 1):
        print()
        tbwsp.append(float(input(f"Współczynnik przy potędze {n - i}: ")))
    x = float(input("Argument: "))
    
    drukujw(n, tbwsp)
    cout << "\ndla x = " << x << " wynosi: ";
    cout << horner_it(n, tbwsp, x) << endl;
    return 0

main()
