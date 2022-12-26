#include <iostream>
#include "pol.h"
using namespace std;

void show_who(Base& r)
{
	r.who();
}

int main()
{
	//Base *p_base;
	//Base base_obj;
	//First first_obj;
	//Second second_obj;

	//p_base = &base_obj;
	//p_base->who();
	//p_base = &first_obj;
	//p_base->who();
	//p_base = &second_obj;
	//p_base->who();

	Base base_obj;
	First first_obj;
	Second second_obj;

	show_who(base_obj);
	show_who(first_obj);
	show_who(second_obj);

	return 0;
}