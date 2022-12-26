#include "figure.h"
#include <iostream>
#include <string>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	vector<figure*> figures;
	point a2(4, 0), b2(0, 0);
	point a1(1, 1), b1(1, 4), c1(5, 4), d1(5, 1);
	point a(4, 0), b(0, 0), c(0, 2), d(0, 0);
	Circle circle1(4.0);
	Circle circle2(a2, b2);
	Rectangle rec1(3.0, 4.0);
	Rectangle rec2(a1, b1, c1, d1);

	Ellipse ell1(4, 2);
	Ellipse ell2(a, b, c, d);

	Triangle tri1(5.0, 4.0, 3.0);

	//figures.push_back(&circle1);
	//figures.push_back(&circle2);
	//figures.push_back(&rec1);
	//figures.push_back(&rec2);
	//double sq = 0.0;
	//for (int i = 0; i < figures.size(); i++)
	//{
	//	sq += figures[i]->calc_perimetr();
	//	cout << "sq" << i << " = " << figures[i]->calc_perimetr() << endl;
	//}
	//cout << "total = " << sq << endl;

	rec1.name();
	cout << rec1.calc_perimetr() << endl;
	cout << rec2.calc_perimetr() << endl;
	cout << rec1.calc_area() << endl;
	cout << rec2.calc_area() << endl;

	ell1.name();
	cout << ell1.calc_perimetr() << endl;
	cout << ell1.calc_area() << endl;
	cout << ell2.calc_area() << endl;

	circle1.name();
	cout << circle1.calc_perimetr() << endl;
	cout << circle2.calc_perimetr() << endl;
	cout << circle1.calc_area() << endl;
	cout << circle2.calc_area() << endl;

	tri1.name();
	//cout << tri1.calc_perimetr() << endl;
	//cout << tri2.calc_perimetr() << endl;
	//cout << tri1.calc_area() << endl;
	//cout <<tri2.calc_area() << endl;
	

	return 0;
		}


