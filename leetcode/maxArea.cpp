#include "ContainerWithMostWater.h"

using namespace std;
/*
因为：contain = min(height[i], height[j]) * (j - i);
所以：if height[i] > height[j], 若 i++ ， contain2 <= height[j] * (j - i - 1) < height[j] * (j - i)
	  if height[j] > height[i], 同上
*/
int maxArea(vector<int> &height)
{
	int maxWater = 0;
	size_t n = height.size();
	size_t i = 0;
	size_t j = n - 1;

	while (i < j)
	{
		int min = height[i] > height[j] ? height[j] : height[i];
		int contain = min * (j - i);
		if (contain > maxWater)	maxWater = contain;
		if (height[j] > height[i])
		{
			++i;
		}
		else
		{
			--j;
		}
	}


	return maxWater;
}
