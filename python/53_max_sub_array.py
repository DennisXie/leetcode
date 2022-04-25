from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        last = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            last = max(nums[i], last+nums[i])
            if last > maximum:
                maximum = last
        return maximum


if __name__ == "__main__":
    print(Solution().maxSubArray([5, 4, -1, 7, 8]))
