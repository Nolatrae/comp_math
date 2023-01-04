#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;
const int scr_width = 80;      // размер консольного окна
const int scr_height = 25;     // размер консольного окна
const int cell_width = 8;      // размер клетки с содержимым
const int cell_height = 5;	   // размер клетки с содержимым
const int field_width = 4;     // размер игрового пол€ в клетках
const int field_height = 4;    // размер игрового пол€ в клетках

typedef char TSscreenMap[scr_height][scr_width]; //хранит символы дл€ вывода на экран

void SetCurPos(int x, int y) // помещает курсор в заданную точку экрана
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

class TScreen//класс дл€ вывода в консольное окно
{
	void SetEnd() { scr[scr_height - 1][scr_width - 1] = '\0'; } // записывает последний элемент в символ конца строки
public:
	TSscreenMap scr; // хранит двумерный массив символов, расположенных на экране
	TScreen() { Clear(); }
	void Clear() { memset(scr, ' ', sizeof(scr)); } // заполн€ет массив пробелами
	void Show() { SetCurPos(0, 0); SetEnd(); cout << scr[0]; }//¬ыводит массив на экран
};

class TCell // класс дл€ отображени€ клеточек
{
public:
	int value; // значение клеточки
	POINT pos; // положение клеточки на экране
	TCell() { Init(0, 0, 0); }
	void Init(int x, int y, int val) { value = val; pos = POINT{x, y}; } // задает параметры клеточки
	void Put(TSscreenMap scr); // рисует клеточку на экран
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
	TScreen screen;	// создали класс
	TCell cell;
	cell.Init(2, 2, 77);
	cell.Put(screen.scr);
	screen.Show(); // отображаем на экране
	getchar(); // ждЄм нажати€ на кнопку
	return 0;
}

