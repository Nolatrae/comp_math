#include <iostream>
#include <windows.h>
#include <cstdio>
#include <cmath>
#include <string> 

#include "2048.h"



int main()
{
	Tgame game;
	while (1)
	{
		game.Work();
		game.Show();
		if (GetKeyState(VK_ESCAPE) < 0) break;
		Sleep(10);
	}
	return 0;
}

