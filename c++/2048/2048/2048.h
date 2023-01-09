#ifndef _2048_
#define _2048_

using namespace std;
const int cons_width = 80;      // размер консольного окна в символах
const int cons_height = 40;     // размер консольного окна в символах
const int cell_width = 8;      // размер клетки с содержимым
const int cell_height = 5;	   // размер клетки с содержимым
const int fld_size = 4;     // размер игрового поля в клетках

namespace foo
{
extern int score;
extern int maxScore;
}

typedef char typeBuffer[cons_height][cons_width]; // тип данных, который хранит символы для вывода на экран 

class consoleView//класс для вывода в консольное окно
{
	void endStroke(); // записывает в последний элемент символ конца строки
public:
	typeBuffer buffer; // хранит двумерный массив символов, нарисованных на экране
	consoleView(); // конструктор
	void Clear();// заполняет массив пробелами
	void Show(); // Выводит массив на экран
	void showScore(); // Выводит счёт на экран
};

class Cell // класс для отображения клеточек
{
public:
	int value; // значение клеточки
	POINT pos; // положение клеточки на экране
	Cell(); // конструктор
	void Init(int x, int y, int val); // задает параметры клеточки
	void Draw(typeBuffer buffer); // рисует клеточку в буфер(buffer) на экран 
}; 

class AnimCell : public Cell //наследник для анимации перемещения || каждя клеточку создаёт анимацию перемещения
{
	float ax, ay; // положение анимированной клеточки
	float dx, dy; // изменение положения
	float aCnt; // количество шагов(кадров)
	int numDuringAnim; // число, которое будет показываться во время анимации
public:
	AnimCell() : Cell() { aCnt = 0; }
	void Anim(POINT to); //логика анимации кеточки в точку to
	bool IsAnim() { return aCnt > 0; } // проверяет есть ли сейчас анимация клеточки
	bool IsState() { return (dx == 0 && dy == 0); } //проверяет, что у клеточки нет перемещения
	void Work() { aCnt--; ax += dx; ay += dy; } // изменяет координаты при анимации
	void DrawAnim(typeBuffer buffer); // рисует анимацию клеточки || отображение анимации
	void DrawState(typeBuffer buffer); // рисует клеточки, которые стоят на месте
};

class Game
{
	consoleView view; // буфер вывода, через неё игра будет показывать себя на экране
	AnimCell cell[fld_size][fld_size]; // массив клеточек = игровое поле
	bool MoveVallInArray(AnimCell *valArr[], int cnt); // механика перемещения чисел в одномерном массиве
	void Move(int dx, int dy); // управление перемещением чисел на карте
	void generateNewNumber(bool anim = false); // создаёт числа в разных клеточках
	int GetFreeCellCnt(); // возращает количество пустых клеточек на карте
	bool CheckEndGame(); // проверяет завершение игры
public:
	Game() { Init(); }
	void Init(); //инициализация игры // задаём позицию клеточек для поля
	void Work(); // нажатия клавиатуры
	void Show(); // отображение игры на экране
};


void ShowPreview();
void ShowEndGame(bool checkEnd = false);
#endif // 