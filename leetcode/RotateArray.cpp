#include "RotateArray.h"

using namespace std;

void RotateArray::rotate(vector<int> &nums, int k)
{
	k = k % nums.size();
	while (k)
	{
		int temp = nums.back();
		nums.pop_back();
		nums.insert(nums.begin(), temp);
		--k;
	}
}

void RotateArray::rotate(int *nums, int numsSize, int k)
{
	k = k % numsSize;
	int temp = 0;
	int i = 0;
	int j = 0;
	int *tempArray = (int *)malloc(k * sizeof(int));
	for (i = numsSize - 1, j = k - 1; j >= 0; --i, --j)
	{
		tempArray[j] = nums[i];
	}

	for (i = numsSize - k - 1; i >= 0; --i)
	{
		nums[i + k] = nums[i];
	}

	for (i = k - 1; i >= 0; --i)
	{
		nums[i] = tempArray[i];
	}

	free(tempArray);
}