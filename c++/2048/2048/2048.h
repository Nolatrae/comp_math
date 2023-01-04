#ifndef _2048_
#define _2048_

//#include <iostream>
//#include <windows.h>
//#include <cstdio>
//#include <cmath>
//#include <string>


using namespace std;
const int scr_width = 60;      // ������ ����������� ����
const int scr_height = 50;     // ������ ����������� ����
const int cell_width = 8;      // ������ ������ � ����������
const int cell_height = 5;	   // ������ ������ � ����������
const int fld_width = 4;     // ������ �������� ���� � �������
const int fld_height = 4;    // ������ �������� ���� � �������

typedef char TSscreenMap[scr_height][scr_width]; //������ ������� ��� ������ �� �����

class TScreen//����� ��� ������ � ���������� ����
{
	void SetEnd(); // ���������� ��������� ������� � ������ ����� ������
public:
	TSscreenMap scr; // ������ ��������� ������ ��������, ������������� �� ������
	TScreen();
	void Clear();
	void Show();
};

class TCell // ����� ��� ����������� ��������
{
public:
	int value; // �������� ��������
	POINT pos; // ��������� �������� �� ������
	TCell();
	void Init(int x, int y, int val); // ������ ��������� ��������
	void Put(TSscreenMap scr); // ������ �������� �� ����� 
};

class TAnimatedCell : public TCell // ����� �������� ������ �������� �����������
{
	float ax, ay; // ��������� ������������� ��������
	float dx, dy; // ��������� ��������� �� ������ ����
	float aCnt; // ���������� �����
	int faceVal; // �����, ������� ����� ������������ �� ����� ��������
public:
	TAnimatedCell() : TCell() { aCnt = 0; }
	void Anim(POINT to); //�������� ������� � ����� to
	bool IsAnim() { return aCnt > 0 ? true : false; } // ��������� ����� �� �������� ��������
	bool IsState() { return (dx == 0 && dy == 0) ? true : false; } //���������, ��� � �������� ��� �����������
	void Work() { aCnt--; ax += dx; ay += dy; } // �������� ���������� ��� ��������
	void PutAnim(TSscreenMap scr); // ������ �������� �������� || ����������� ��������
	void PutState(TSscreenMap scr); // ������ ��������, ������� ����� �� �����
};

class Tgame
{
	TScreen screen;
	TAnimatedCell cell[fld_height][fld_width];
	//TCell cell[fld_height][fld_width]; // ������ �������� = ������� ����
	//bool MoveVallInArray(TCell* valArr[], int cnt); // �������� ����������� 
	bool MoveVallInArray(TAnimatedCell *valArr[], int cnt);
	void Move(int dx, int dy); // ���������� ������������ ����� �� �����
	void GenNewRandNum(bool anim = false); // ������ ����� � ������ ���������
	//void GenNewRandNum(); // ������ ����� � ������ ���������

	int GetFreeCellCnt(); // ��������� ���������� ������ �������� �� �����
	bool CheckEndGame();
public:
	Tgame() { Init(); }
	void Init(); //������������
	void Work();
	void Show(); // ����������� ���� �� ������
};


#endif // 