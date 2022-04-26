from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_right = 0
        ans = 0

        for i in range(len(prices)-1, -1, -1):
            if max_right - prices[i] > ans:
                ans = max_right - prices[i]

            if prices[i] > max_right:
                max_right = prices[i]

        return ans


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 6, 5, 2, 8]))
