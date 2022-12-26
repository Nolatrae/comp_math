#ifndef _pol_
#define _pol_

#include <iostream>
#include <string>

using namespace std;

class Base
{
public:
	virtual void who();
};

class First : public Base
{
public:
	void who();
};

class Second : public First
{
public:
	void who();
};



#endif // 