from typing import List


class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        descent_len = 0
        for i in range(len(prices)):
            if i-1 < 0 or prices[i] == prices[i-1] - 1:
                descent_len += 1
            else:
                count = count + (1 + descent_len) * descent_len // 2
                descent_len = 1
        else:
            count = count + (1 + descent_len) * descent_len // 2
        return count

if __name__ == "__main__":

    print(Solution().getDescentPeriods([4, 3, 2, 1, 4]))
