#ifndef _2048_
#define _2048_

//#include <iostream>
//#include <windows.h>
//#include <cstdio>
//#include <cmath>
//#include <string>


using namespace std;
const int cons_width = 80;      // ������ ����������� ���� 
const int cons_height = 40;     // ������ ����������� ����
const int cell_width = 8;      // ������ ������ � ����������
const int cell_height = 5;	   // ������ ������ � ����������
const int fld_width = 4;     // ������ �������� ���� � �������
const int fld_height = 4;    // ������ �������� ���� � �������


namespace foo
{
extern int hitCnt;
extern int maxHitCnt;
}


typedef char TSscreenMap[cons_height][cons_width]; // ��� ������, ������� ������ ������� ��� ������ �� ����� 

class TScreen//����� ��� ������ � ���������� ����
{
	void endStroke(); // ���������� � ��������� ������� ������ ����� ������
public:
	TSscreenMap scr; // ������ ��������� ������ ��������, ������������ �� ������
	TScreen(); // �����������
	void Clear();// ��������� ������ ���������
	void Show(); // ������� ������ �� �����
	void showScore(); // ������� ���� �� �����
};

class TCell // ����� ��� ����������� ��������
{
public:
	int value; // �������� ��������
	POINT pos; // ��������� �������� �� ������
	TCell(); // �����������
	void Init(int x, int y, int val); // ������ ��������� ��������
	void Put(TSscreenMap scr); // ������ �������� � �����(scr) �� ����� 
}; 

class TAnimatedCell : public TCell //��������� ��� �������� ����������� || ����� �������� ������ �������� �����������
{
	float ax, ay; // ��������� ������������� ��������
	float dx, dy; // ��������� ���������
	float aCnt; // ���������� �����(������)
	int faceVal; // �����, ������� ����� ������������ �� ����� ��������
public:
	TAnimatedCell() : TCell() { aCnt = 0; }
	void Anim(POINT to); //�������� ������� � ����� to
	bool IsAnim() { return aCnt > 0; } // ��������� ���� �� ������ �������� ��������
	bool IsState() { return (dx == 0 && dy == 0); } //���������, ��� � �������� ��� �����������
	void Work() { aCnt--; ax += dx; ay += dy; } // �������� ���������� ��� ��������
	void PutAnim(TSscreenMap scr); // ������ �������� �������� || ����������� ��������
	void PutState(TSscreenMap scr); // ������ ��������, ������� ����� �� �����
};

class Tgame
{
	//Tgame() { int fld_width = 4; int fld_height = 4; }
	TScreen screen; // ����� ������, ����� �� ���� ����� ���������� ���� �� ������
	TAnimatedCell cell[fld_height][fld_width]; // ������ �������� = ������� ����
	//TAnimatedCell cell[int fld_width][int fld_width]; // ������ �������� = ������� ����

	bool MoveVallInArray(TAnimatedCell *valArr[], int cnt); // �������� ����������� ����� � ���������� �������
	//bool MoveVallInArray(TAnimatedCell* valArr[], TAnimatedCell* previousField[], int cnt); // �������� ����������� ����� � ���������� �������

	void Move(int dx, int dy); // ���������� ������������ ����� �� �����
	void GenNewRandNum(bool anim = false); // ������ ����� � ������ ���������
	int GetFreeCellCnt(); // ��������� ���������� ������ �������� �� �����
	bool CheckEndGame(); // ��������� ���������� ����
public:
	Tgame() { Init(); }
	void Init(); //������������� ���� // ����� ������� �������� ��� ����
	void Work(); // ������� ����������
	void Show(); // ����������� ���� �� ������
};


void ShowPreview();
void ShowEndGame(bool checkEnd = false);
//int hitCnt = 0;
#endif // 