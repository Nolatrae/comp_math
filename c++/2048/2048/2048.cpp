#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string>

#include <conio.h>

#define KEY_UP 72
#define KEY_DOWN 80
#define KEY_LEFT 75
#define KEY_RIGHT 77

#include "2048.h"

using namespace std;

int foo::hitCnt = 0;

void SetCurPos(int x, int y) // помещает курсор в заданную точку экрана
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void TScreen::SetEnd()
{
	scr[scr_height - 1][scr_width - 1] = '\0'; // записывает последний элемент в символ конца строки
}

TScreen::TScreen()
{
	Clear();
}

void TScreen::Clear()
{
	memset(scr, ' ', sizeof(scr)); // заполняет массив пробелами
}

void TScreen::Show()
{
	SetCurPos(0, 0); SetEnd(); cout << scr[0];//Выводит массив на экран
}


TCell::TCell()
{
	Init(0, 0, 0);
}

void TCell::Init(int x, int y, int val)
{
	value = val; pos = POINT{ x, y };
}

void TCell::Put(TSscreenMap scr)
{
	for (int i = 0; i < cell_width; i++) // строим границы клетки плюсиками, иначе оставляем пробелы
		for (int j = 0; j < cell_height; j++)
			scr[pos.y + j][pos.x + i] = (i == 0 || i == cell_width - 1 ||
										 j == 0 || j == cell_height - 1) ? '+' : ' ';
	if (value == 0)	return; // если число равно 0, то выходим
	char buf[10]; //иначе переводим число в строку
	sprintf_s(buf, "%d", value);
	int len = strlen(buf);
	int posX = (cell_width - len) / 2;
	int posY = (cell_height - 1) / 2;// находим середину
	for (int i = 0; i < len; i++)
 		scr[pos.y + posY][pos.x + i + posX] = buf[i]; // выводим число в массив
}


////*valArr[] это массив указателей на клеточки, cnt - это длина массива\

bool Tgame::MoveVallInArray(TAnimatedCell* valArr[], int cnt)
{	
	//int score = 0;
	bool moved = false; ////moved говорит о том,что некоторые цифры на поле сместились
	int lastX = 0; //позиция последней клетки, в которую можно перенести циферки
	for (int i = 1; i < cnt; i++) //проходим по всему массиву
		if (valArr[i]->value != 0) // если значение текущей клетки != 0
		{						  // то проверяем значение последней клеточки
			if (valArr[lastX]->value == 0)
			{
				valArr[i]->Anim(valArr[lastX]->pos);
				valArr[lastX]->Anim(valArr[lastX]->pos);
				moved = true;
				valArr[lastX]->value = valArr[i]->value;// помещаем значение текущей клетки в последнюю
				valArr[i]->value = 0; // а значение текущей сбрасываем в 0
			}
			else
			{
				if (valArr[lastX]->value == valArr[i]->value) //если значение последней и текущей ячейки совпадают
				{
					valArr[i]->Anim(valArr[lastX]->pos);
					valArr[lastX]->Anim(valArr[lastX]->pos);
					moved = true;
					valArr[lastX]->value += valArr[i]->value; //то просто складываем их в последней ячейке
					foo::hitCnt += valArr[lastX]->value;
					//cout << valArr[lastX]->value << endl; //////////////////////////////////////////////////////////////////////////////////
					valArr[i]->value = 0; //текущую обнуляем
					lastX++;
					score += 1;
				}
				else
				{
					if (valArr[lastX]->value != valArr[i]->value)//если значение последней и текущей ячейки  НЕ совпадают
					{
						lastX++; // последняя ячейка переходит на следующую 
						if (lastX != i) // изменения будут в том случае, если это всё таки разные ячейки
						{
							valArr[i]->Anim(valArr[lastX]->pos);
							valArr[lastX]->Anim(valArr[lastX]->pos);
							moved = true;
							valArr[lastX]->value = valArr[i]->value; // передвигаем значение
							valArr[i]->value = 0;//текущую обнуляем
						}
					}
				}
			}
		}
	return moved;
}

void Tgame::Move(int dx, int dy) // dx and xy говорят о том куда надо подвинуть цифры
{
	bool moved = false;
	if (dx != 0) // двигаем фифры влево по оси Х
		for (int j = 0; j < fld_height; j++) // проходим по оси У
		{
			TAnimatedCell* valArr[fld_width];
			for (int i = 0; i < fld_width; i++)
			{
				int x = (dx < 0) ? i : fld_width - i - 1;
				valArr[i] = &cell[j][x];
			}
			if (MoveVallInArray(valArr, fld_width)) moved = true;
		}

	if (dy != 0) // двигаем цифры влево по оси Y
		for (int i = 0; i < fld_width; i++) // проходим по оси X
		{
			TAnimatedCell* valArr[fld_height];
			for (int j = 0; j < fld_height; j++)
			{
				int y = (dy < 0) ? j : fld_height - j - 1;
				valArr[j] = &cell[y][i];
			}
			if (MoveVallInArray(valArr, fld_height)) moved = true;
		}
	if (CheckEndGame())
	{
		Init();
		//if (hitCnt > maxHitCnt)
		//{
		//	maxHitCnt = hitCnt;
		//}
		//	hitCnt = 0;
	}
	else
		if (moved) //если было передвижение, то добавляем число на поле
			GenNewRandNum(true);
}


void Tgame::GenNewRandNum(bool anim)
{
	if (GetFreeCellCnt() == 0) return;// если пустых клеток нет то выходим
	int cnt = 1;
	while (cnt > 0)
	{
		//иначе ищем случайную пустую клетку
		int x = rand() % fld_width;
		int y = rand() % fld_height;
		if (cell[y][x].value == 0)
		{
			if (anim)
				cell[y][x].Anim(cell[y][x].pos);
			cell[y][x].value = (rand() % 10 == 0) ? 4 : 2, cnt--;//кладём 2 или 4
		}
	}//4 генерирутеся только в 10% случаев
}

int Tgame::GetFreeCellCnt()
{
	int cnt = 0;
	for (int i = 0; i < fld_width * fld_height; i++)
		if (cell[0][i].value == 0)
			cnt++;
	return cnt;
}

bool Tgame::CheckEndGame()
{
	if (GetFreeCellCnt() > 0) //если пустых клеток больше 1
		return false;
	for (int i = 0; i < fld_width; i++)
		for (int j = 0; j < fld_height; j++) // проходим по всему игровому полю
			if ((j < fld_height - 1 && cell[j][i].value == cell[j + 1][i].value) || //смотрим соседние клетки, если есть одинаковые значит ещё можно сделать ход
				(i < fld_width - 1 && cell[j][i].value == cell[j][i + 1].value))
				return false;
	return true;
}

bool KeyDownOnce(char c)
{
	if (GetKeyState(c) < 0)
	{
		while (GetKeyState(c) < 0);
		return true;
	}
	return false;
}

void Tgame::Init()
{
	const int dx = 2;
	const int dy = 2;
	srand(GetTickCount());
	for (int i = 0; i < fld_width; i++)
		for (int j = 0; j < fld_height; j++)
			cell[j][i].Init(dx + i * (cell_width - 1), dy + j * (cell_height - 1), 0);
	GenNewRandNum();
	GenNewRandNum();
}

void Tgame::Work()
{
	if (KeyDownOnce('W') || (GetKeyState(VK_UP) < 0)) Move(0, -1);
	if (KeyDownOnce('S') || (GetKeyState(VK_DOWN) < 0)) Move(0, 1);
	if (KeyDownOnce('A') || (GetKeyState(VK_LEFT) < 0)) Move(-1, 0);
	if (KeyDownOnce('D') || (GetKeyState(VK_RIGHT) < 0)) Move(1, 0);
}

//void Tgame::Score()
//{
//	cout << rand() % fld_width;
//}  


void Tgame::Show()
{
	for (int i = 0; i < fld_width * fld_height; i++) cell[0][i].PutState(screen.scr);
	for (int i = 0; i < fld_width * fld_height; i++) cell[0][i].PutAnim(screen.scr);
	//cout << score << endl;
	screen.Show();
}

void TAnimatedCell::Anim(POINT to)
{
	if (IsAnim()) return; // если клетка анимирована, то анимацию не добавляем
	faceVal = value;
	aCnt = 20;
	ax = pos.x;
	ay = pos.y;
	dx = (to.x - ax) / (float)aCnt; // двигаем позицию клетки от начальной до позиции to
	dy = (to.y - ay) / (float)aCnt;
}

void TAnimatedCell::PutAnim(TSscreenMap scr)
{
	if (IsAnim())
	{
		Work();
		if (IsState()) return;
		TCell cell;
		cell.Init( lround(ax), lround(ay), faceVal);
		cell.Put(scr);
	}
}

void TAnimatedCell::PutState(TSscreenMap scr)
{
	if (IsAnim())
	{
		TCell cell;
		if (IsState())
			cell.Init(pos.x, pos.y, faceVal);
		else
			cell.Init(pos.x, pos.y, 0);
		cell.Put(scr);
	}
	else
		Put(scr);
}



void ShowPreview()
{
	system("cls");
	printf("\n\n\n\n\n\n\n\n\n\n\n\n \t\t\t\t    2048");
	//for (int i = 0; i < 10; i++) {
	//	cout << '\n';
	//	for (int j = 0; j < 5; j++) {
	//		cout << '\n';
	//		if (j == 4) {
	//		cout << "2048";
	//		}
	//	}
	//}
	Sleep(1000);
	system("cls");
}
