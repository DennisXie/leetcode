#include "SortColors.h"

using namespace std;

void SortColors::sortColors(vector<int> &nums)
{
	size_t count[3] = { 0, 0, 0 };
	for (vector<int>::value_type i : nums)
	{
		++count[i];
	}

	for (vector<int>::value_type &i : nums)
	{
		if (count[0])
		{
			--count[0];
			i = 0;
		}
		else if (count[1])
		{
			--count[1];
			i = 1;
		}
		else if (count[2])
		{
			--count[2];
			i = 2;
		}
	}
}