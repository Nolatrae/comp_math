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
		game.Work(); // ������� �������
		game.Show(); // ������� ������
		//game.Score();

		//cout << score << endl;
		if (GetKeyState(VK_ESCAPE) < 0) break; // ����������� ��������� �������
		Sleep(10); // ��������� ��������
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

