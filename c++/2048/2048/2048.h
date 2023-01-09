#ifndef _2048_
#define _2048_

using namespace std;
const int cons_width = 80;      // ������ ����������� ���� � ��������
const int cons_height = 40;     // ������ ����������� ���� � ��������
const int cell_width = 8;      // ������ ������ � ����������
const int cell_height = 5;	   // ������ ������ � ����������
const int fld_size = 4;     // ������ �������� ���� � �������

namespace foo
{
extern int score;
extern int maxScore;
}

typedef char typeBuffer[cons_height][cons_width]; // ��� ������, ������� ������ ������� ��� ������ �� ����� 

class consoleView//����� ��� ������ � ���������� ����
{
	void endStroke(); // ���������� � ��������� ������� ������ ����� ������
public:
	typeBuffer buffer; // ������ ��������� ������ ��������, ������������ �� ������
	consoleView(); // �����������
	void Clear();// ��������� ������ ���������
	void Show(); // ������� ������ �� �����
	void showScore(); // ������� ���� �� �����
};

class Cell // ����� ��� ����������� ��������
{
public:
	int value; // �������� ��������
	POINT pos; // ��������� �������� �� ������
	Cell(); // �����������
	void Init(int x, int y, int val); // ������ ��������� ��������
	void Draw(typeBuffer buffer); // ������ �������� � �����(buffer) �� ����� 
}; 

class AnimCell : public Cell //��������� ��� �������� ����������� || ����� �������� ������ �������� �����������
{
	float ax, ay; // ��������� ������������� ��������
	float dx, dy; // ��������� ���������
	float aCnt; // ���������� �����(������)
	int numDuringAnim; // �����, ������� ����� ������������ �� ����� ��������
public:
	AnimCell() : Cell() { aCnt = 0; }
	void Anim(POINT to); //������ �������� ������� � ����� to
	bool IsAnim() { return aCnt > 0; } // ��������� ���� �� ������ �������� ��������
	bool IsState() { return (dx == 0 && dy == 0); } //���������, ��� � �������� ��� �����������
	void Work() { aCnt--; ax += dx; ay += dy; } // �������� ���������� ��� ��������
	void DrawAnim(typeBuffer buffer); // ������ �������� �������� || ����������� ��������
	void DrawState(typeBuffer buffer); // ������ ��������, ������� ����� �� �����
};

class Game
{
	consoleView view; // ����� ������, ����� �� ���� ����� ���������� ���� �� ������
	AnimCell cell[fld_size][fld_size]; // ������ �������� = ������� ����
	bool MoveVallInArray(AnimCell *valArr[], int cnt); // �������� ����������� ����� � ���������� �������
	void Move(int dx, int dy); // ���������� ������������ ����� �� �����
	void generateNewNumber(bool anim = false); // ������ ����� � ������ ���������
	int GetFreeCellCnt(); // ��������� ���������� ������ �������� �� �����
	bool CheckEndGame(); // ��������� ���������� ����
public:
	Game() { Init(); }
	void Init(); //������������� ���� // ����� ������� �������� ��� ����
	void Work(); // ������� ����������
	void Show(); // ����������� ���� �� ������
};


void ShowPreview();
void ShowEndGame(bool checkEnd = false);
#endif // 