#include "figure.h"
#include <iostream>
#include <string>
#include<math.h>
#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES

double vector_lenght(const point& p1, const point& p2) {
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double geron(const point& p1, const point& p2, const point& p3) {
	return ((p2.x - p1.x)*(p3.y - p1.y) - (p3.x-p1.x)*(p2.y - p1.y)) / 2;
}

double vector_distance(const point& p) {
	return sqrt((0 - p.x) * (0 - p.x) + (0 - p.y) * (0 - p.y));
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
Rectangle::Rectangle(const point& a, const point& b, const point& c, point& d){
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
//Triangle::Triangle(const point& a, const point& b, const point& c)
//{
//	points.resize(3);
//	points[0] = a;
//	points[1] = b;
//	points[2] = c;
//}
//
//double Triangle::calc_area()
//{
//	using st = StorageType;
//	switch (m_type)
//	{
//	case st::Points: {
//		return geron(points[0], points[1], points[2]);
//	} break;
//	case st::Lines: {
//		return sqrt(poluperimetr(a, b, c) * (poluperimetr(a, b, c) - a) * (poluperimetr(a, b, c) - b) * (poluperimetr(a, b, c) - c));
//	} break;
//	}
//}

void Triangle::name()
{
	cout << "Треугольник" << endl;
}
