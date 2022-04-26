from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # general solution for stock problem
        k = 2
        # f[i][j][0] represents the max profit of i th day have done j transaction and don't hold any stock
        # f[i][j][1] represents the max profit of i th day have done j transaction and hold stock
        # f[0][j][0] = 0, f[0][j][1] = -prices[0]  the first day we can't sell stock, we can only buy stock
        # f[i][0][0] = 0, f[i][0][1] = 0   j = 0 means doesn't do any transaction
        f = [[[0] * 2 for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(1, k+1):
                if i - 1 < 0:
                    # the first day to buy and sell
                    f[i][j][0] = 0
                    f[i][j][1] = -prices[i]
                    continue
                # sell stocks, we can  +prices[i] because we -prices[i-xx] when we buy.
                # So the profit will be prices[i] - prices[i-xx]
                #                still hold,    sell
                f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1] + prices[i])
                #                still hold,    buy
                f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0] - prices[i])
        return f[len(prices)-1][k][0]

    def maxProfit2(self, prices: List[int]) -> int:
        k = 2
        f = [[[0] * 2 for _ in range(k+1)] for _ in range(2)]

        # the current state is only related to previous state, so we can use rolling array
        idx = 0
        for i in range(len(prices)):
            for j in range(1, k+1):
                if i - 1 < 0:
                    f[i][j][0] = 0
                    f[i][j][1] = -prices[i]
                else:
                    f[idx][j][0] = max(f[1-idx][j][0], f[1-idx][j][1] + prices[i])
                    f[idx][j][1] = max(f[1-idx][j][1], f[1-idx][j-1][0] - prices[i])
            print(f[idx])
            idx = 1 - idx
        return f[1-idx][k][0]

    def maxProfit3(self, prices: List[int]) -> int:
        k = 2
        f = [[0] * 2 for _ in range(k+1)]

        for i in range(len(prices)):
            # because the previous state never used again and loop j from k to 1 to avoid influencing the current state
            # calculation
            for j in range(k, 0, -1):
                if i - 1 < 0:
                    f[j][0] = 0
                    f[j][1] = -prices[i]
                else:
                    f[j][0] = max(f[j][0], f[j][1] + prices[i])
                    f[j][1] = max(f[j][1], f[j-1][0] - prices[i])
        return f[k][0]


if __name__ == "__main__":
    print(Solution().maxProfit2([3, 3, 5, 0, 0, 3, 1, 4]))
    print(Solution().maxProfit3([3, 3, 5, 0, 0, 3, 1, 4]))
