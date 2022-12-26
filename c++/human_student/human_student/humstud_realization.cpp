#include "human_student.h"                                                           
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

human::human(string last_name, string name, string second_name)
{
	this->last_name = last_name;
	this->name = name;
	this->second_name = second_name;
}

string human::get_full_name()
{
	ostringstream full_name;
	full_name << this->last_name << " " << this->name << " " << this->second_name;
	return full_name.str();
}


//student::student(string last_name, string name, string second_name, vector<int> scores) : human(last_name, name, second_name)
//{
//	this->scores = scores;
//}

float student::get_average_score()
{
	unsigned int count_scores = this->scores.size();
	unsigned int sum_scores = 0;
	float average_score;

	for (unsigned int i = 0; i < count_scores; i++) {
		sum_scores += this->scores[i];
	}

	average_score = (float)sum_scores / (float)count_scores;
	return average_score;
}