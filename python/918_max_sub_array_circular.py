from typing import List


class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        last = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            last = max(nums[i], last + nums[i])
            maximum = max(maximum, last)

        right = [None] * len(nums)
        max_right = [None] * len(nums)
        right[-1] = nums[-1]
        max_right[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] + nums[i]
            max_right[i] = max(max_right[i+1], right[i])

        left = 0
        for i in range(len(nums)-2):
            left += nums[i]
            # left + max_right[i+1]即为整个区间，第一步就能算出来
            if left + max_right[i+2] > maximum:
                maximum = left + max_right[i+2]

        return maximum


if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([1, 2, 3, 4]))
    print(Solution().maxSubarraySumCircular([1, -1, 3, 4]))
    print(Solution().maxSubarraySumCircular([5, -3, 5]))
