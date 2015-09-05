#include "RotateImage.h"

void rotate(int **matrix, int matrixRowSize, int matrixColSize)
{
	int i, j, k, x, y;
	int temp;
	int n = matrixColSize;
	for (i = 0; i < matrixRowSize / 2; ++i)
	{
		for (j = i; j < matrixColSize - i - 1; ++j)
		{
			x = j;
			y = matrixColSize - 1 - i;
			for (k = 0; k < 3; ++k)
			{
				temp = *(matrix + x * n +y);
				matrix[x][y] = matrix[i][j];
				matrix[i][j] = temp;
				temp = y;
				y = matrixColSize - 1 - x;
				x = temp;
			}
		}
	}
}
