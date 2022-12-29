#include "figure_2_real.h"
#include <iostream>
#include <string>
#include<math.h>
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
class File_Exception {};

double vector_lenght(const point& p1, const point& p2) {
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double geron(const point& p1, const point& p2, const point& p3) {
	return ((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)) / 2;
}


double poluperimetr(double a, double b, double c)
{
	return (a + b + c) / 2;
}


///////////////////////////////////////////////////////////////////////////////////////////////
Circle::Circle(const point& a, point& b)
{
	points.resize(2);
	points[0] = a;
	points[1] = b;
}

double Circle::calc_area()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return vector_lenght(points[0], points[1]) * M_PI * vector_lenght(points[0], points[1]);
	} break;
	case st::Lines: {
		return R * R * M_PI;
	} break;
	}
}

double Circle::calc_perimetr()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return vector_lenght(points[0], points[1]) * M_PI * 2;
	} break;
	case st::Lines: {
		return 2 * R * M_PI;
	} break;
	}

}

void Circle::name()
{
	cout << "Круг" << endl;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
Ellipse::Ellipse(const point& a, const point& b, const point& c, point& d) {
	points.resize(4);
	points[0] = a;
	points[1] = b;
	points[2] = c;
	points[3] = d;
}


double Ellipse::calc_area()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return (vector_lenght(points[0], points[1]) * vector_lenght(points[1], points[2])) * M_PI;
	} break;
	case st::Lines: {
		return a * b * M_PI;
	} break;
	}
}
//double Ellipse::calc_area()
//{
//	return a * b * M_PI;
//}

double Ellipse::calc_perimetr()
{
	//using st = StorageType;
	//switch (m_type)
	//{
	//case st::Points: {
	//	//a = vector_lenght(points[0], points[1]);
	//	//b = vector_lenght(points[2], points[3]);
	//	return 2 * M_PI * sqrt((vector_lenght(points[0], points[1]) * vector_lenght(points[0], points[1]) + vector_lenght(points[2], points[3]) * vector_lenght(points[2], points[3])) / 2);
	//} break;
	//case st::Lines: {
	//	return 2 * M_PI * sqrt((a * a + b * b) / 2);
	//} break;
	//}
	return 2 * M_PI * sqrt((a * a + b * b) / 2);

}

void Ellipse::name()
{
	cout << "Элипс" << endl;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////
Rectangle::Rectangle(const point& a, const point& b, const point& c, point& d) {
	points.resize(4);
	points[0] = a;
	points[1] = b;
	points[2] = c;
	points[3] = d;
}


double Rectangle::calc_area()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return vector_lenght(points[0], points[1]) * vector_lenght(points[1], points[2]);
	} break;
	case st::Lines: {
		return a * b;
	} break;
	}
}

double Rectangle::calc_perimetr()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return 2 * (vector_lenght(points[0], points[1]) + vector_lenght(points[1], points[2]));
	} break;
	case st::Lines: {
		return 2 * (a + b);
	} break;
	}
}

void Rectangle::name()
{
	cout << "Прямоугольник" << endl;
}
//////////////////////////////////////////////////////////////////////////
Triangle::Triangle(const point& a, const point& b, const point& c)
{
	points.resize(3);
	points[0] = a;
	points[1] = b;
	points[2] = c;
}

double Triangle::calc_area()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return geron(points[0], points[1], points[2]);
	} break;
	case st::Lines: {
		return sqrt(poluperimetr(a, b, c) * (poluperimetr(a, b, c) - a) * (poluperimetr(a, b, c) - b) * (poluperimetr(a, b, c) - c));
	} break;
	}
}

double Triangle::calc_perimetr()
{
	using st = StorageType;
	switch (m_type)
	{
	case st::Points: {
		return (vector_lenght(points[0], points[1]) + vector_lenght(points[1], points[2]) + vector_lenght(points[0], points[2]));
	} break;
	case st::Lines: {
		return poluperimetr(a, b, c) * 2;
	} break;
	}
}

void Triangle::name()
{
	cout << "Треугольник" << endl;
}


Polygon::Polygon(vector<point> _points)
{

		points = _points;
		size = points.size();
		points.resize(size + 1);
		points[size] = points[0];
}

Polygon::Polygon(char* filename)
{
	{
		ifstream in;
		in.open(filename, std::ios::in);
		if (in.is_open()) {
			string line;
			getline(in, line);

			stringstream sstream(line);
			size_t str_size;
			sstream >> str_size;
			size = str_size;
			points.resize(size + 1);
			int i = 0;
			while (i != size + 1) {
				int x, y;
				in >> x >> y;
				points[i] = point(x, y);
				i++;
			}
		}
		else {
			throw File_Exception();
		}
	}
}

void Polygon::name()
{
	{ cout << "Многоугольник" << endl; }
}

double Polygon::calc_perimetr()
{
	double sum = 0;
	for (int i = 0; i < size; i++)
	{
		sum += vector_lenght(points[i], points[i + 1]);
	}
	return sum;
}

double Polygon::calc_area()
{
	int sum = 0;
	for (int i = 1; i <= size; i++)
	{
		sum += (points[i - 1].x * points[i].y - points[i - 1].y * points[i].x);
	}
	return abs((double)sum / 2);
}



