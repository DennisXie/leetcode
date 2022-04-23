from typing import List

class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[mid-1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid
            else:
                return mid
        return left
