#ifndef _figure_
#define _figure_
#include <iostream>
#include <string>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
using namespace std;

struct point {
	double x, y;
	point() : x(0), y(0) {};
	point(double ax, double ay) : x(ax), y(ay) {};
};

class figure
{
protected:
	int nodeCount;
	//point* points;
	vector <point> points;
public:
	virtual double calc_area() = 0;
	virtual double calc_perimetr() = 0;
	virtual void name() = 0;
	friend double vector_lenght(const point& p1, const point& p2);
};

class Circle : public figure
{
public:
	enum class StorageType {
		Points,
		Lines
	};
	double R;
	Circle() { R = 0.0; m_type = StorageType::Lines;}
	Circle(double _R) { R = _R; m_type = StorageType::Lines;};
	Circle(const point& a, point& b);
	double calc_area();
	double calc_perimetr();
	void name();
private:
	StorageType m_type;
};

class Ellipse : public figure
{
public:
	enum class StorageType {
		Points,
		Lines
	};
	double a, b;
	Ellipse() { a = b = 0.0; m_type = StorageType::Lines;};
	Ellipse(double _a, double _b) { a = _a, b = _b; m_type = StorageType::Lines;};
	Ellipse(const point& a, const point& b, const point& c, point& d);
	double calc_area();
	double calc_perimetr();
	void name();
private:
	StorageType m_type;
};

class Rectangle : public figure
{

public:
	enum class StorageType {
		Points,
		Lines
	};

	double a, b;
	Rectangle() { a = b = 0.0; m_type = StorageType::Lines;};
	Rectangle(double _a, double _b) { a = _a, b = _b; m_type = StorageType::Lines;};
	Rectangle(const point& a, const point& b, const point& c, point& d);
	double calc_area();
	double calc_perimetr();
	void name();
private:
	StorageType m_type;
};

class Triangle : public figure
{
public:
	enum class StorageType {
		Points,
		Lines
	};
	double a, b, c;
	Triangle() { a = b = c = 0.0; m_type = StorageType::Lines; };
	Triangle(double _a, double _b, double _c) { a = _a, b = _b, c = _c; m_type = StorageType::Lines; };
	Triangle(const point& a, const point& b, const point& c);
	double calc_area();
	//double calc_perimetr();
	void name();
private:
	StorageType m_type;
};
#endif // 
