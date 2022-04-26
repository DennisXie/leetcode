from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            cur = prices[i] - prices[i-1]
            if cur > 0:
                profit += cur
        return profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4, 9, 9, 0]))
