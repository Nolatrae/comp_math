#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string> 
#include<cstdlib>
#include<ctime>

#include "2048.h"



int main()
{
	//ShowPreview();

	TScreen screen;
	//screen.scr[6][6] = 'E';
	//screen.scr[8][8] = 'E';
	//screen.Show();

	//int width, height;
	//cout << "¬ведите ширину пол€ - " << endl;
	//cin >> width;
	//cout << "¬ведите высоту пол€ - " << endl;
	//cin >> height;

	Tgame game;
	while (1)
	{
		game.Work(); // нажатие клавиши
		game.Show(); // процесс работы
		if (GetKeyState(VK_ESCAPE) < 0) // отслеживает состо€ние клавиши
		{
			ShowEndGame(true);
			break;
		}
		Sleep(10); // плавность анимации
	}

	//TCell cell;
	//cell.Init(6, 6, 77);
	//cell.Put(screen.scr);
	//cell.Init(10, 10, 15);
	//cell.Put(screen.scr);
	//screen.Show();

	//cout << hitCnt << ' ' << maxHitCnt << endl;
	//cout << foo::hitCnt << endl;
	//int score = 3;
	//int* scorePTR = NULL;
	//scorePTR = &score;
	//*scorePTR = 1 + *scorePTR;
	//cout << *scorePTR;
	//cout << game.score << endl;
	return 0;
}

