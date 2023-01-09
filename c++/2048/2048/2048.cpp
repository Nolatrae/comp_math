#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string>
#include<cstdlib>
#include<ctime>
#include <conio.h>

#include "2048.h"

using namespace std;

int foo::hitCnt = 0;
int foo::maxHitCnt = 0;

void setCursor(int x, int y) // помещает курсор в заданную точку экрана
{
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void TScreen::endStroke()
{
	scr[cons_height - 1][cons_width - 1] = '\0'; // записывает в последний элемент символ конца строки
}

TScreen::TScreen() // конструктор
{
	Clear();
}

void TScreen::Clear() // заполняет массив пробелами
{
	memset(scr, ' ', sizeof(scr)); 
}

void TScreen::Show()
{
	setCursor(0, 0); endStroke(); cout << scr[0];//Выводит массив на экран
}

void TScreen::showScore()
{
	setCursor(fld_width * 10, 10); endStroke(); cout << "Score: " << foo::hitCnt;
	setCursor(fld_width * 10, 11); endStroke(); cout << "MAX Score: " << foo::maxHitCnt;
	setCursor(0, 30); endStroke();
}
  
///////////////////////////////////////////////////////////////////////////////////////////

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
	for (int i = 0; i < cell_width; i++) // проходим по всем символам одной клеточки
		for (int j = 0; j < cell_height; j++) // проходим по всем символам одной клеточки
			if(i == 0 || i == cell_width - 1 || j == 0 || j == cell_height - 1) // если это крайние символы клетки
			{ 
				scr[pos.y + j][pos.x + i] = '+';  //строим границы клетки плюсиками
			}
			else
			{
				scr[pos.y + j][pos.x + i] = ' '; // иначе ставим пробелы
			}
			//scr[pos.y + j][pos.x + i] = (i == 0 || i == cell_width - 1 || j == 0 || j == cell_height - 1) ? '+' : ' '; // зная позицию клеточки, строим границы клетки плюсиками если это крайние символы, иначе оставляем пробелы
	if (value == 0)	return; // если число равно 0, то выходим
	char buf[10]; 
	sprintf_s(buf, "%d", value); //иначе переводим число в строку
	int len = strlen(buf); // считаем длину строки
	int posX = (cell_width - len) / 2; // находим позицию вывода числа для середины
	int posY = (cell_height - 1) / 2;// находим позицию вывода числа для середины
	for (int i = 0; i < len; i++)
 		scr[pos.y + posY][pos.x + i + posX] = buf[i]; // выводим число в буфер
}

///////////////////////////////////////////////////////////////////////////////////////////

////*valArr[] это массив указателей на клеточки
// cnt - длина массива
bool Tgame::MoveVallInArray(TAnimatedCell* valArr[], int cnt)
{
	bool moved = false; ////moved говорит о том,что некоторые цифры на поле сместились
	int lastX = 0; //позиция последней клетки, в которую можно перенести циферки
	for (int i = 1; i < cnt; i++) //проходим по всему массиву
		if (valArr[i]->value != 0) // если значение текущей клетки != 0
		{						  // то проверяем значение последней клеточки
			if (valArr[lastX]->value == 0) // если последняя клетка равна 0
			{
				valArr[i]->Anim(valArr[lastX]->pos); // текущая клеточка создаст анимацию перемещения в позицию другой клетки
				valArr[lastX]->Anim(valArr[lastX]->pos); // исправление бага с клеточкой || клеточка появлялась на новом месте раньше, чем приезжала
				moved = true;
				valArr[lastX]->value = valArr[i]->value;// помещаем значение текущей клетки в последнюю
				valArr[i]->value = 0; // а значение текущей сбрасываем в 0
			}
			else
			{
				if (valArr[lastX]->value == valArr[i]->value) // если значение последней и текущей ячейки совпадают
				{
					valArr[i]->Anim(valArr[lastX]->pos); // текущая клеточка создаст анимацию перемещения в позицию другой клетки
					valArr[lastX]->Anim(valArr[lastX]->pos); // исправление бага с клеточкой || клеточка появлялась на новом месте раньше, чем приезжала
					moved = true;
					valArr[lastX]->value += valArr[i]->value; // то складываем их в последней ячейке
					valArr[i]->value = 0; // текущую обнуляем
					foo::hitCnt += valArr[lastX]->value; // проверка на максимальный счёт
					if (foo::hitCnt > foo::maxHitCnt)
					{
						foo::maxHitCnt = foo::hitCnt;
					}
					lastX++; // в последнюю ячейку нельзя ничего записывать, переходим к следующей
				}
				else
				{
					if (valArr[lastX]->value != valArr[i]->value)// если значение последней и текущей ячейки  НЕ совпадают
					{
						lastX++; // последняя ячейка переходит на следующую 
						if (lastX != i) // изменения будут в том случае, если это всё таки разные ячейки || защита от одной и той же ячейки 
						{
							valArr[i]->Anim(valArr[lastX]->pos); // текущая клеточка создаст анимацию перемещения в позицию другой клетки
							valArr[lastX]->Anim(valArr[lastX]->pos); // исправление бага с клеточкой || клеточка появлялась на новом месте раньше, чем приезжала
							moved = true;
							valArr[lastX]->value = valArr[i]->value; // передвигаем значение
							valArr[i]->value = 0;// текущую обнуляем
						}
					}
				}
			}
		}
	return moved;
}

void Tgame::Move(int dx, int dy) // dx and xy говорят о том куда надо подвинуть цифры
{
	int x, y;
	bool moved = false;
	if (dx != 0) // двигаем цифры  по оси Х
		for (int j = 0; j < fld_height; j++) // проходим по оси У
		{
			TAnimatedCell* valArr[fld_width]; // массив указателей на клеточки
			for (int i = 0; i < fld_width; i++)
			{
				if (dx < 0) // если двигаем влево
				{
					x = i; // то в массив записываем значения от 1 до последней
				}
				else
				{
					x = fld_width - i - 1; // иначе от последней до первой
				}
				//int x = (dx < 0) ? i : fld_width - i - 1; // если двигаем влево то в массив записываем значения от 1 до последней, иначе от последней до первой
				valArr[i] = &cell[j][x]; // записываем адреса всех клеточек строки
			}
			if (MoveVallInArray(valArr, fld_width)) moved = true;
			// вызываем функци, которая двигает числа в массиве клеточек
		} 

	if (dy != 0) // двигаем цифры по оси Y
		for (int i = 0; i < fld_width; i++) // проходим по оси X
		{
			TAnimatedCell* valArr[fld_height]; // массив указателей на клеточки
			for (int j = 0; j < fld_height; j++)
			{
				if (dy < 0)
				{
					y = j; // сверху вниз
				}
				else
				{
					y = fld_height - j - 1; // снизу вверх
				}
				//int y = (dy < 0) ? j : fld_height - j - 1; // сверху вниз, снизу вверх
				valArr[j] = &cell[y][i]; // записываем адреса каждой клеточки столбца записываем в массив
			}
			if (MoveVallInArray(valArr, fld_height)) moved = true; // вызываем функцию, которая двигает числа в массиве клеточек
		}
	if (CheckEndGame())
	{
		ShowEndGame(false);
		Init();

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
		if (cell[x][y].value == 0)
		{
			if (anim)
				cell[x][y].Anim(cell[x][y].pos); // значение появится после анимации, во время анимации клетка будет пустая
			cell[x][y].value = (rand() % 10 == 0) ? 4 : 2, cnt--;//кладём 2 или 4, делаем cnt--, для того чтобы выйти из цикла
		}
	}//4 генерирутеся только в 10% случаев
}

int Tgame::GetFreeCellCnt()
{
	int cnt = 0; // количество пустых клеточек
	for (int i = 0; i < fld_width; i++)  // проходим по всему массиву поля
		for (int j = 0; j < fld_height; j++) // проходим по всему массиву поля
			if (cell[i][j].value == 0)
			cnt++;
	return cnt;
}

bool Tgame::CheckEndGame()
{
	if (GetFreeCellCnt() > 0) //если пустых клеток больше 1
		return false;
	for (int i = 0; i < fld_width; i++) // проходим по всему игровому полю
		for (int j = 0; j < fld_height; j++) // проходим по всему игровому полю
			if ((j < fld_height - 1 && cell[j][i].value == cell[j + 1][i].value) || //смотрим соседние клетки, если есть одинаковые значит ещё можно сделать ход
				(i < fld_width - 1 && cell[j][i].value == cell[j][i + 1].value)) // fld_height - 1, чтобы не было проблем с массивом
				return false;
	return true;
}


bool KeyDownOnce(char c)  // функция однократного нажатия на кнопку
{
	if (GetKeyState(c) < 0)
	{
		while (GetKeyState(c) < 0); // выполняем цикл пока кнопка нажата
		return true;
	}
	return false;
} 

void Tgame::Init()
{
	if (foo::hitCnt > foo::maxHitCnt) // проверка условия максимального счёта
	{
		foo::maxHitCnt = foo::hitCnt;
	}
	//foo::hitCnt = 0;
	foo::hitCnt = 0; // счётчик
	const int dx = 1; // начало вывода игрового поля
	const int dy = 1; // начало вывода игрового поля
	//srand(time(NULL)); // инициализируем рандомайзер
	for (int i = 0; i < fld_width; i++) // проходим по полю клеток
		for (int j = 0; j < fld_height; j++) // проходим по полю клеток
			cell[i][j].Init(dx + j * (cell_width - 1), dy + i * (cell_height - 1), 0); //задаём позицию клеточек для поля || -1 у сторон прописан для объединения клеток
	GenNewRandNum();
	GenNewRandNum();
}

void Tgame::Work()
{
	if (KeyDownOnce('W') || (GetKeyState(VK_UP) < 0)) Move(0, -1);
	if (KeyDownOnce('S') || (GetKeyState(VK_DOWN) < 0)) Move(0, 1);
	if (KeyDownOnce('A') || (GetKeyState(VK_LEFT) < 0)) Move(-1, 0);
	if (KeyDownOnce('D') || (GetKeyState(VK_RIGHT) < 0)) Move(1, 0);
	if (KeyDownOnce('R')) Init();
}

void Tgame::Show()
{
	for (int i = 0; i < fld_width; i++)
		for (int j = 0; j < fld_height; j++)
			cell[i][j].PutState(screen.scr);

	for (int i = 0; i < fld_width; i++)
		for (int j = 0; j < fld_height; j++)
			cell[i][j].PutAnim(screen.scr);

	screen.Show();
	screen.showScore();
}

///////////////////////////////////////////////////////////////////////////////////////////

void TAnimatedCell::Anim(POINT to)
{
	if (IsAnim()) return; // если клетка анимирована, то анимацию не добавляем
	faceVal = value;
	aCnt = 15; // количество шагов(кадров)
	ax = pos.x; // тут мы сейчас
	ay = pos.y; // тут мы сейчас
	dx = (to.x - ax) / (float)aCnt; // двигаем позицию клетки от начальной до позиции to
	dy = (to.y - ay) / (float)aCnt;
}

void TAnimatedCell::PutAnim(TSscreenMap scr)
{
	if (IsAnim()) // проверяет идёт ли анимация клетки прямо сейчас
	{
		Work(); // если идёт, то двигаем анимацию
		if (IsState()) return; // если клетка статична, значит она уже была анимирована в PutState 
		TCell cell; // рисуем клетку в заданном месте с заданным значением
		cell.Init( lround(ax), lround(ay), faceVal); // lround - Возвращает целое значение, ближайшее к x || нужен, для исправления бага с полем
		cell.Put(scr);
	}
}

void TAnimatedCell::PutState(TSscreenMap scr)
{
	if (IsAnim()) // проверяет есть ли сейчас анимация клеточки
	{
		TCell cell;
		if (IsState()) // но анимацию проходит без движения
			cell.Init(pos.x, pos.y, faceVal); // рисуем клеточку с указанным значение в анимации
		else
			cell.Init(pos.x, pos.y, 0); // отображаем пустое поле, тк клеточка уехала
		cell.Put(scr);
	}
	else
		Put(scr); // если анимации нет, то рисуем поле как обычно
}

///////////////////////////////////////////////////////////////////////////////////////////

void ShowPreview()
{
	system("cls");
	printf("\n\n\n\n\n\n\n\n\n\n\n\n \t\t\t\t    2048");
	Sleep(1000);
	system("cls");
}  

void ShowEndGame(bool checkEnd)
{
	system("cls");
	if (checkEnd) {
		printf("\n\n\n\n\n\n\n\n\n\n\n\n \t\t\t    Your max score - %d", foo::maxHitCnt);

	}
	else {
	printf("\n\n\n\n\n\n\n\n\n\n\n\n \t\t\t    Your score - %d", foo::hitCnt);
	}
	Sleep(2000);
	system("cls");
}

//TAnimatedCell previousGame(TAnimatedCell* previousField[][])
//{
//	return;
//}

// обоснованность решения алгоритма( для того чтобы это работало, я использовал такой тип данных, ну к примеру)
// программа не должна крашиться от лишних нажатий
// память время устойчивость, почему такие структуры данных именно
// будут разные входные данные, упасть на них она конечно не должна