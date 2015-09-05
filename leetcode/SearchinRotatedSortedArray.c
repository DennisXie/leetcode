#include "SearchinRotatedSortedArray.h"

int binarySearch(int *nums, int start, int end, int target)
{
	int idx_head = start - 1, idx_tail = end + 1;

	while (idx_head < idx_tail - 1)
	{
		int mid = (idx_head + idx_tail) >> 1;
		if (target == nums[mid])
		{
			return mid;
		}
		else if (target < nums[mid])
		{
			idx_tail = mid;
		}
		else if (target > nums[mid])
		{
			idx_head = mid;
		}
	}

	return -1;
}

int search(int *nums, int numsSize, int target)
{
	if (numsSize == 0) return -1;

	int idx_head, idx_tail;
	idx_head = 0;
	idx_tail = numsSize - 1;

	while (idx_head < idx_tail)
	{
        if (idx_head == idx_tail - 1) break;
		int mid = (idx_head + idx_tail) >> 1;
		if (nums[mid] > nums[idx_head]) idx_head = mid;
		if (nums[mid] <= nums[idx_tail]) idx_tail = mid;
	}

	int idx_min = idx_tail;
	int idx_max = idx_tail - 1;

	if (idx_tail == idx_head || nums[0] < nums[numsSize - 1]) return binarySearch(nums, 0, numsSize - 1, target);

	if (target >= nums[0]) return binarySearch(nums, 0, idx_max, target);
	if (target <= nums[numsSize - 1]) return binarySearch(nums, idx_min, numsSize - 1, target);
    return -1;
}