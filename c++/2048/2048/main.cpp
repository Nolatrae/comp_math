#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string> 

#include "2048.h"



int main()
{
	ShowPreview();
	Tgame game;
	while (1)
	{
		game.Work(); // нажатие клавиши
		game.Show(); // процесс работы
		//game.Score();

		//cout << score << endl;
		if (GetKeyState(VK_ESCAPE) < 0) break; // отслеживает состояние клавиши
		Sleep(10); // плавность анимации
	}
	//cout << hitCnt << ' ' << maxHitCnt << endl;
	cout << foo::hitCnt << endl;

	//int score = 3;
	//int* scorePTR = NULL;
	//scorePTR = &score;
	//*scorePTR = 1 + *scorePTR;
	//cout << *scorePTR;
	//cout << game.score << endl;
	return 0;
}

