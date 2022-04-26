from typing import List

class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        f = [[0, 0], [0, 0]]
        idx = 0
        for i in range(len(prices)):
            if i - 1 < 0:
                f[idx][0] = 0
                f[idx][1] = -prices[i]
            else:
                f[idx][0] = max(f[1-idx][0], f[1-idx][1]+prices[i]-fee)
                f[idx][1] = max(f[1-idx][1], f[1-idx][0]-prices[i])
            idx = 1 - idx
        return f[1-idx][0]


if __name__ == "__main__":
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
