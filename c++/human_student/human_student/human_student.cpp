#include <iostream>
#include <vector>
#include <locale.h>
#include "human_student.h"
using namespace std;


int main(int argc, char* argv[])
{
    setlocale(LC_ALL, "Russian");

    vector<int> scores;

    scores.push_back(5);
    scores.push_back(3);
    scores.push_back(5);
    scores.push_back(5);
    scores.push_back(3);
    scores.push_back(4);
    scores.push_back(5);
    scores.push_back(4);
    scores.push_back(5);

    student* stud = new student("Ежов", "Егор", "Александрович", scores);

    cout << stud->get_full_name() << endl;

    cout << "Средний балл: " << stud->get_average_score() << endl;

    system("pause");


    return 0;
}