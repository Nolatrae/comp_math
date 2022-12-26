#include "pol.h"
#include <iostream>
#include <string>
using namespace std;

void Base::who()
{
	cout << "Base\n";
}

void First::who()
{
	cout << "First derivation\n";
}

void Second::who()
{
	cout << "second derivation\n";
}

