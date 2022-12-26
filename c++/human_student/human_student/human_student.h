#ifndef _human_student_
#define _human_student_

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

class human
{
private:
	string name;
	string last_name;
	string second_name;
public:
	human(string last_name, string name, string second_name);
	string get_full_name();
};


class student : public human
{
private:
	vector<int> scores;

public:
	student(string last_name, string name, string second_name, vector<int> scores) : human(last_name, name, second_name)
	{
		this->scores = scores;
	}
	float get_average_score();
};

#endif // 
