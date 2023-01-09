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

	//consoleView view;
	//view.buffer[6][6] = 'E';
	//view.buffer[8][8] = 'E';
	//view.Show();  
	 
	//consoleView view;
	//Cell cell;
	//cell.Init(6, 6, 35);
	//cell.Draw(view.buffer);
	//cell.Init(10, 10, 15);
	//cell.Draw(view.buffer);
	//view.Show();

	ShowPreview();
	Game game;
	while (1)
	{
		game.Work(); // нажатие клавиши
		game.Show(); // процесс работы
		if (GetKeyState(VK_ESCAPE) < 0) // отслеживает состояние клавиши
		{
			ShowEndGame(true);
			break;
		}
		Sleep(10);
	}


	return 0;
}

