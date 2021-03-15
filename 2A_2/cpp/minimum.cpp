/*
 * minimum.cpp
 * 
 * Copyright 2020  <>
 * 
 */

#include <iostream>
using namespace std;

int minimum2(int t[], int n)
{
	int min = t[0];
	for (int i = 1; i < n; i++)
	{
		if (t[i] < min)
			min = t[i];
	}
	return min;
}

void pobierzLiczby(int t[], int n)
{
	cout << "Podaj liczby: ";
	for (int i = 0; i < n; i++)
	{
		cin >> t[i];
	}
}

int minimum1(int n)
{
	int x, min;
	cout << "Podaj liczbę: ";
	cin >> min;
	for (int i = 1; i < n; i++)
	{
		cout << "Podaj liczbę: ";
		cin >> x;
		if (x < min)
			min = x;
	}
	return min;
}

int main(int argc, char **argv)
{
	int n, min;
	cout << "Ile podasz liczb? ";
	cin >> n;
	int t[n];
	//min = minimum1(n);
	pobierzLiczby(t, n);
	min = minimum2(t, n);
	cout << "Najmniejsza liczba: " << min << endl;
	return 0;
}

