from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == nums[j]:
                j = j - 1
            elif nums[i] < nums[j]:
                break
            else:
                mid = (i + j) // 2
                if nums[mid] > nums[i]:
                    i = mid
                elif nums[mid] < nums[j]:
                    j = mid
                elif nums[mid] == nums[i]:
                    i = i + 1
                else:
                    j = j - 1
        return nums[i]


if __name__ == "__main__":
    # print(Solution().findMin([1, 2, 3, 4]))
    # print(Solution().findMin([1, 1, 2, 3, 4]))
    # print(Solution().findMin([1, 2, 2, 3, 4]))
    print(Solution().findMin([4, 1, 1, 2, 3]))
    print(Solution().findMin([4, 1, 1, 2, 3, 4]))
    print(Solution().findMin([0, 0, 0, 0, 0]))
    print(Solution().findMin([3, 3, 0, 1, 2]))
    print(Solution().findMin([3, 3, 3, 1, 2]))
    print(Solution().findMin([3, 3, 2, 2, 2]))
