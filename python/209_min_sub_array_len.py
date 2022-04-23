from typing import List

class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        count = nums[0]
        if count >= target:
            return 1

        min_length = len(nums)
        while i <= j < len(nums):
            print(i, j, count)
            if count < target:
                j += 1
                if j == len(nums):
                    return 0
                count += nums[j]
            elif count >= target:
                if j - i + 1 < min_length:
                    min_length = j - i + 1
                if count - nums[i] >= target:
                    count -= nums[i]
                    i += 1
                else:
                    j += 1
                    if j == len(nums):
                        return min_length
                    count += nums[j]
        return min_length


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
