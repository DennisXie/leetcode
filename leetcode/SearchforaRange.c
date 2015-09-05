#include "SearchforaRange.h"

int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{
    int *ans = (int *)malloc(2 * sizeof(int));
    ans[0] = -1;
    ans[1] = -1;
    *returnSize = 2;

    if (numsSize == 0) return ans;

    int idx_begin = -1, idx_end = numsSize;
    while (idx_begin != idx_end - 1)
    {
        int mid = (idx_begin + idx_end) >> 1;
        if (nums[mid] < target) idx_begin = mid;
        if (nums[mid] >= target) idx_end = mid;
    }
    ans[0] = (idx_end < numsSize && nums[idx_end] == target) ? idx_end : -1;

    idx_begin = -1;
    idx_end = numsSize;
    while (idx_begin != idx_end - 1)
    {
        int mid = (idx_begin + idx_end) >> 1;
        if (nums[mid] <= target) idx_begin = mid;
        if (nums[mid] > target) idx_end = mid;
    }
    ans[1] = (idx_begin >= 0 && nums[idx_begin] == target) ? idx_begin : -1;

    *returnSize = 2;
    return ans;
}