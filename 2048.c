#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;
const int scr_width = 80;      // ������ ����������� ����
const int scr_height = 25;     // ������ ����������� ����
const int cell_width = 8;      // ������ ������ � ����������
const int cell_height = 5;	   // ������ ������ � ����������
const int field_width = 4;     // ������ �������� ���� � �������
const int field_height = 4;    // ������ �������� ���� � �������

typedef char TSscreenMap[scr_height][scr_width]; //������ ������� ��� ������ �� �����

void SetCurPos(int x, int y) // �������� ������ � �������� ����� ������
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

class TScreen//����� ��� ������ � ���������� ����
{
	void SetEnd() { scr[scr_height - 1][scr_width - 1] = '\0'; } // ���������� ��������� ������� � ������ ����� ������
public:
	TSscreenMap scr; // ������ ��������� ������ ��������, ������������� �� ������
	TScreen() { Clear(); }
	void Clear() { memset(scr, ' ', sizeof(scr)); } // ��������� ������ ���������
	void Show() { SetCurPos(0, 0); SetEnd(); cout << scr[0]; }//������� ������ �� �����
};

class TCell // ����� ��� ����������� ��������
{
public:
	int value; // �������� ��������
	POINT pos; // ��������� �������� �� ������
	TCell() { Init(0, 0, 0); }
	void Init(int x, int y, int val) { value = val; pos = POINT{x, y}; } // ������ ��������� ��������
	void Put(TSscreenMap scr); // ������ �������� �� �����
};

void TCell::Put(TSscreenMap scr)
{
	for (int i = 0; i < cell_width; i++)
		for (int j = 0; j < cell_height; j++)
			scr[pos.y + j][pos.x + i] = (i == 0 || i == cell_width - 1 ||
										 j == 0 || j == cell_height - 1) ? '+' : ' ';
	if (value == 0)	return;
	char buf[10];
	sprintf(buf, "%d", value);
	//to_string(value);
	int len = strlen(buf);
	int posX = (cell_width - len) / 2;
	int posY = (cell_height - 1) / 2;
	for (int i = 0; i < len; i++)
 		scr[pos.y + posY][pos.x + i + posX] = buf[i];
}
int main()
{
	TScreen screen;	// ������� �����
	TCell cell;
	cell.Init(2, 2, 77);
	cell.Put(screen.scr);
	screen.Show(); // ���������� �� ������
	getchar(); // ��� ������� �� ������
	return 0;
}

