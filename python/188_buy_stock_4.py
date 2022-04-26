from typing import List

class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0

        f = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(1, k+1):
                if i - 1 < 0:
                    f[i][j][0] = 0
                    f[i][j][1] = -prices[i]
                else:
                    f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1] + prices[i])
                    f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0] - prices[i])
        return f[len(prices)-1][k][0]


if __name__ == "__main__":
    print(Solution().maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
