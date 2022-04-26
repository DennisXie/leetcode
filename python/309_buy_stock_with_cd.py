from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

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

    def maxProfit2(self, prices: List[int]) -> int:

        f = [[0, 0] for _ in range(len(prices))]
        for i in range(len(prices)):
            if i - 1 < 0:
                f[i][0] = 0
                f[i][1] = -prices[i]
            else:
                # Note: this is the mathematical explanation why we can use only 0 1 rather than 0, 1, 2
                # The state transition formula is written in the maxProfit.
                # f[i][0] = max(f[i-1][0], f[i-1][2])
                # f[i][1] = max(f[i-1][1], f[i-1][0]-prices[i], f[i-2][2]-prices[i])
                # f[i][2] = f[i-1][1]+prices[i]
                # So f[i-1][2] = f[i-2][1]+prices[i-1]
                #    f[i-2][2] = f[i-3][1]+prices[i-2]
                #    f[i-1][0] = max(f[i-2][0], f[i-2][2]) = max(f[i-2][0], f[i-3][1]+prices[i-2])
                #    f[i-2][0] = max(f[i-3][0], f[i-3][2]) = max(f[i-3][0], f[i-4][1]+prices[i-3])
                # Then we can have the following:
                # f[i][0] = max(f[i-1][0], f[i-1][2]) = max(f[i-1][0], f[i-2][1]+prices[i-1])
                # f[i][1] = max(f[i-1][1], f[i-1][0]-prices[i], f[i-3][1]+prices[i-2]-prices[i])
                # so we can avoid sell status. we can have new formula
                # f[i][0/2] = max(f[i-1][0], f[i-2][1]+prices[i-1], f[i-1][1]+prices[i])
                #           = max(f[i-1][0], f[i-1][1]+prices[i]) because f[i-1][0] = max(f[i-2][1]+prices[i-1], ...)
                # f[i][1] = max(f[i-1][1], f[i-2][0/2]-prices[i]) because f[i-2][0/2] = max(f[i-3][1]+prices[i-2], ...)

                f[i][0] = max(f[i-1][0], f[i-1][1]+prices[i])
                f[i][1] = max(f[i-1][1], f[i-2][0]-prices[i])

        return f[len(prices)-1][0]


if __name__ == "__main__":
    print(Solution().maxProfit2([1]))
    print(Solution().maxProfit2([1, 2, 3, 0, 2]))
