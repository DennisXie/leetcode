#include "QuickSort.h"

void qsort(int *a, int start, int end)
{
	int x = a[start];
	int i = start, j = end;
	
	while (i < j)
	{
		while (i < j && a[j] > x) --j;
		if (i < j)
		{
			a[i] = a[j];
			++i;
		}

		while (i < j && a[i] < x) ++i;
		if (i < j)
		{
			a[j] = a[i];
			--j;
		}
	}
	a[i] = x;

	if (i - 1 > start) qsort(a, start, i - 1);
	if (j + 1 < end) qsort(a, j + 1, end);
}