#ifndef _2048_
#define _2048_

//#include <iostream>
//#include <windows.h>
//#include <cstdio>
//#include <cmath>
//#include <string>


using namespace std;
const int scr_width = 80;      // размер консольного окна
const int scr_height = 40;     // размер консольного окна
const int cell_width = 8;      // размер клетки с содержимым
const int cell_height = 5;	   // размер клетки с содержимым
const int fld_width = 4;     // размер игрового поля в клетках
const int fld_height = 4;    // размер игрового поля в клетках

//int maxHitCnt = 0;

namespace foo
{
extern int hitCnt;
}


typedef char TSscreenMap[scr_height][scr_width]; //хранит символы для вывода на экран

class TScreen//класс для вывода в консольное окно
{
	void SetEnd(); // записывает последний элемент в символ конца строки
public:
	TSscreenMap scr; // хранит двумерный массив символов, расположенных на экране
	TScreen();
	void Clear();
	void Show();
};

class TCell // класс для отображения клеточек
{
public:
	int value; // значение клеточки
	POINT pos; // положение клеточки на экране
	TCell();
	void Init(int x, int y, int val); // задает параметры клеточки
	void Put(TSscreenMap scr); // рисует клеточку на экран 
};

class TAnimatedCell : public TCell // каждя клеточку создаёт анимацию перемещения
{
	float ax, ay; // положение анимированное клеточки
	float dx, dy; // изменение положения на каждом шагу
	float aCnt; // количество шагов
	int faceVal; // число, которое будет показываться во время анимации
public:
	TAnimatedCell() : TCell() { aCnt = 0; }
	void Anim(POINT to); //анимация кеточки в точку to
	bool IsAnim() { return aCnt > 0 ? true : false; } // проверяет нужна ли анимация клеточки
	bool IsState() { return (dx == 0 && dy == 0) ? true : false; } //проверяет, что у клеточки нет перемещения
	void Work() { aCnt--; ax += dx; ay += dy; } // изменяет координаты при анимации
	void PutAnim(TSscreenMap scr); // рисует анимацию клеточки || отображение анимации
	void PutState(TSscreenMap scr); // рисует клеточки, которые стоят на месте
};

class Tgame
{
	TScreen screen;
	TAnimatedCell cell[fld_height][fld_width]; // массив клеточек = игровое поле
	bool MoveVallInArray(TAnimatedCell *valArr[], int cnt); // механика перемещения 
	void Move(int dx, int dy); // управление перемещением чисел на карте
	void GenNewRandNum(bool anim = false); // создаёт числа в разных клеточках
	int GetFreeCellCnt(); // возращает количество пустых клеточек на карте
	bool CheckEndGame();
public:
	int score;
	Tgame() { Init(); }
	void Init(); //инициаизация
	void Work();
	//void Score();
	void Show(); // отображение игры на экране
};


void ShowPreview();
//int hitCnt = 0;
#endif // 