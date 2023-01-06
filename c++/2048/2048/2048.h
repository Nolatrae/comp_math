#ifndef _2048_
#define _2048_

//#include <iostream>
//#include <windows.h>
//#include <cstdio>
//#include <cmath>
//#include <string>


using namespace std;
const int scr_width = 80;      // ������ ����������� ����
const int scr_height = 40;     // ������ ����������� ����
const int cell_width = 8;      // ������ ������ � ����������
const int cell_height = 5;	   // ������ ������ � ����������
const int fld_width = 4;     // ������ �������� ���� � �������
const int fld_height = 4;    // ������ �������� ���� � �������

//int maxHitCnt = 0;

namespace foo
{
extern int hitCnt;
}


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
	TAnimatedCell cell[fld_height][fld_width]; // ������ �������� = ������� ����
	bool MoveVallInArray(TAnimatedCell *valArr[], int cnt); // �������� ����������� 
	void Move(int dx, int dy); // ���������� ������������ ����� �� �����
	void GenNewRandNum(bool anim = false); // ������ ����� � ������ ���������
	int GetFreeCellCnt(); // ��������� ���������� ������ �������� �� �����
	bool CheckEndGame();
public:
	int score;
	Tgame() { Init(); }
	void Init(); //������������
	void Work();
	//void Score();
	void Show(); // ����������� ���� �� ������
};


void ShowPreview();
//int hitCnt = 0;
#endif // 