from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        mid = 0
        while i <= j:
            mid = (i+j) // 2
            # nums[i] > nums[j]
            if nums[i] > nums[j]:
                if nums[mid] > nums[i]:
                    i = mid
                elif nums[mid] < nums[j]:
                    j = mid
                else:
                    mid = j
                    break
            else:
                mid = i
                break

        return nums[mid]


if __name__ == "__main__":
    print(Solution().findMin([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(Solution().findMin([9, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(Solution().findMin([8, 9, 1, 2, 3, 4, 5, 6, 7]))
    print(Solution().findMin([7, 8, 9, 1, 2, 3, 4, 5, 6]))
    print(Solution().findMin([2, 3, 4, 5, 6, 7, 8, 9, 1]))
