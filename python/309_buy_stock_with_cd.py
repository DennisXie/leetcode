from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1]+prices[i])
        f[i][j][1] = max(f[i-1][j][1], f[i-2][j-1][0]-prices[i])
        pass
