#ifndef _2048_
#define _2048_

//#include <iostream>
//#include <windows.h>
//#include <cstdio>
//#include <cmath>
//#include <string>


using namespace std;
const int cons_width = 80;      // размер консольного окна 
const int cons_height = 40;     // размер консольного окна
const int cell_width = 8;      // размер клетки с содержимым
const int cell_height = 5;	   // размер клетки с содержимым
const int fld_width = 4;     // размер игрового поля в клетках
const int fld_height = 4;    // размер игрового поля в клетках


namespace foo
{
extern int hitCnt;
extern int maxHitCnt;
}


typedef char TSscreenMap[cons_height][cons_width]; // тип данных, который хранит символы для вывода на экран 

class TScreen//класс для вывода в консольное окно
{
	void endStroke(); // записывает в последний элемент символ конца строки
public:
	TSscreenMap scr; // хранит двумерный массив символов, нарисованных на экране
	TScreen(); // конструктор
	void Clear();// заполняет массив пробелами
	void Show(); // Выводит массив на экран
	void showScore(); // Выводит счёт на экран
};

class TCell // класс для отображения клеточек
{
public:
	int value; // значение клеточки
	POINT pos; // положение клеточки на экране
	TCell(); // конструктор
	void Init(int x, int y, int val); // задает параметры клеточки
	void Put(TSscreenMap scr); // рисует клеточку в буфер(scr) на экран 
}; 

class TAnimatedCell : public TCell //наследник для анимации перемещения || каждя клеточку создаёт анимацию перемещения
{
	float ax, ay; // положение анимированной клеточки
	float dx, dy; // изменение положения
	float aCnt; // количество шагов(кадров)
	int faceVal; // число, которое будет показываться во время анимации
public:
	TAnimatedCell() : TCell() { aCnt = 0; }
	void Anim(POINT to); //анимация кеточки в точку to
	bool IsAnim() { return aCnt > 0; } // проверяет есть ли сейчас анимация клеточки
	bool IsState() { return (dx == 0 && dy == 0); } //проверяет, что у клеточки нет перемещения
	void Work() { aCnt--; ax += dx; ay += dy; } // изменяет координаты при анимации
	void PutAnim(TSscreenMap scr); // рисует анимацию клеточки || отображение анимации
	void PutState(TSscreenMap scr); // рисует клеточки, которые стоят на месте
};

class Tgame
{
	//Tgame() { int fld_width = 4; int fld_height = 4; }
	TScreen screen; // буфер вывода, через неё игра будет показывать себя на экране
	TAnimatedCell cell[fld_height][fld_width]; // массив клеточек = игровое поле
	//TAnimatedCell cell[int fld_width][int fld_width]; // массив клеточек = игровое поле

	bool MoveVallInArray(TAnimatedCell *valArr[], int cnt); // механика перемещения чисел в одномерном массиве
	//bool MoveVallInArray(TAnimatedCell* valArr[], TAnimatedCell* previousField[], int cnt); // механика перемещения чисел в одномерном массиве

	void Move(int dx, int dy); // управление перемещением чисел на карте
	void GenNewRandNum(bool anim = false); // создаёт числа в разных клеточках
	int GetFreeCellCnt(); // возращает количество пустых клеточек на карте
	bool CheckEndGame(); // проверяет завершение игры
public:
	Tgame() { Init(); }
	void Init(); //инициализация игры // задаём позицию клеточек для поля
	void Work(); // нажатия клавиатуры
	void Show(); // отображение игры на экране
};


void ShowPreview();
void ShowEndGame(bool checkEnd = false);
//int hitCnt = 0;
#endif // 