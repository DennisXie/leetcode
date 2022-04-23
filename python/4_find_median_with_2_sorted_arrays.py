from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self._single_num(nums2)
        elif len(nums2) == 0:
            return self._single_num(nums1)

        if nums2[-1] < nums1[0]:
            nums1, nums2 = nums2, nums1

        self.odd = True if (len(nums1) + len(nums2)) & 1 == 1 else False

        pn1 = int(len(nums1) / 2)
        pn2 = int(len(nums2) / 2)
        # TODO: len(nums1) == 0 or len(num2) == 0
        count = 0
        while not self._check_valid(nums1[:pn1], nums1[pn1:], nums2[:pn2], nums2[pn2:]) and count < 6:
            count += 1
            if nums1[pn1-1] > nums2[pn2]:
                pn1 = int(pn1 / 2)
                pn2 = int((pn2 + len(nums2)) / 2)
            elif nums2[pn2-1] > nums1[pn1]:
                pn1 = int((pn1 + len(nums1)) / 2)
                pn2 = int(pn2 / 2)
            elif self._check_length(pn1 + pn2, len(nums1) + len(nums2) - pn1 - pn2) > 0:
                if nums1[pn1-1] > nums2[pn2-1]:
                    # TODO: what about len(nums2) == 0
                    pn1 -= 1
                else:
                    pn2 -= 1
            elif self._check_length(pn1 + pn2, len(nums1) + len(nums2) - pn1 - pn2) < 0:
                if nums1[pn1] > nums2[pn2]:
                    # TODO: what about len(nums2) == 0
                    pn2 -= 1
                else:
                    pn1 -= 1
        return pn1, pn2
        # return nums1[pn1] if self.odd else (nums1[pn1] + nums2[pn2]) / 2

    def _check_valid(self, left1: List[int], right1: List[int], left2: List[int], right2: List[int]) -> bool:
        print(left1, right1, left2, right2)
        smaller_length = len(left1) + len(left2)
        bigger_length = len(right1) + len(right2)
        length_equal = smaller_length+1 == bigger_length or smaller_length == bigger_length + 1 if self.odd else smaller_length == bigger_length

        left1_right2_valid = False
        left2_right1_valid = False
        if len(left1) > 0:
            if len(right2) > 0:
                left1_right2_valid = left1[-1] < right2[0]
            else:
                left1_right2_valid = True
        else:
            left1_right2_valid = True

        if len(left2) > 0:
            if len(right1) > 0:
                left2_right1_valid = left2[-1] < right1[0]
            else:
                left2_right1_valid = True
        else:
            left2_right1_valid = True

        return length_equal and left1_right2_valid and left2_right1_valid

    def _check_length(self, left, right) -> int:
        equal = left+1 == right or left == right + 1if self.odd else left == right
        if equal:
            return 0
        else:
            return left - right

    def _single_num(self, nums: List[int]) -> float:
        mid = len(nums) >> 1
        if len(nums) & 1 == 0:
            return (nums[mid] + nums[mid-1]) / 2
        else:
            return nums[mid]

    def _calc_median(self, left1: List[int], righ1: List[int], left2: List[int], right2: List[int]) -> float:
        pass


if __name__ == "__main__":
    # print(Solution().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]))
    # print(Solution().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8, 9]))
    print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 7, 9], [6, 8]))
    print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 7, 9, 10], []))
