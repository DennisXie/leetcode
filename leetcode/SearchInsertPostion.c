#include "SearchInsertPosition.h"
#include <stdlib.h>

int searchInsert(int *nums, int numsSize, int target)
{
    if (nums == NULL || numsSize == 0) return 0;

    int low = 0, high = numsSize - 1;

    while (low >= 0 && high < numsSize && low <= high)
    {
        int mid = (low + high) >> 1;
        if (nums[mid] > target)
        {
            high = mid - 1;
        }
        else if (nums[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            return mid;
        }
    }

    return low;
}