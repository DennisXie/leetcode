from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # f[i][j][0] = max(f[i-1][j][0], f[i-1][j][2])    # hold without stock
        # f[i][j][1] = max(f[i-1][j][1], f[i-2][j-1][0]-prices[i])    # buy or hold stock
        # f[i][j][2] = max(f[i-1][j][1]+prices[i])                    # sell

        f = [[0, 0, 0] for _ in range(len(prices))]
        for i in range(len(prices)):
            if i - 1 < 0:
                f[i][0] = 0
                f[i][1] = -prices[i]
                f[i][2] = 0
            else:
                # max(hold without stock, cd)
                f[i][0] = max(f[i-1][0], f[i-1][2])
                # max(hold stock, buy stock after hold, buy stock after cd)
                f[i][1] = max(f[i-1][1], f[i-1][0]-prices[i], f[i-2][2]-prices[i])
                # sell stock
                f[i][2] = f[i-1][1]+prices[i]
        for i in f:
            print(i)
        return max(f[len(prices)-1][0], f[len(prices)-1][2])


if __name__ == "__main__":
    print(Solution().maxProfit([1]))
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
