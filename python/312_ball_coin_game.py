from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] represents i to j max coins can get, i and j are not included which means (i, j)
        # we iterate the last broken ball, so we can confirm the followings:
        # 1. the last broken ball can get coin = nums[k]*nums[i]*nums[j]
        # 2. the left side is dp[i][k]
        # 3. the right side is dp[k][j]
        # the state switching formula dp[i][j] = max(dp[i][k] + dp[k][j] + nums[k]*nums[i]*nums[j])
        nums.append(1)
        nums.insert(0, 1)
        coins = [[-1] * len(nums) for _ in range(len(nums))]

        for i in range(len(nums)-1):
            coins[i][i+1] = 0

        for l in range(2, len(nums)):
            for j in range(2, len(nums)):
                i = j - l
                for k in range(i+1, j):
                    candidate = coins[i][k] + coins[k][j] + nums[k] * nums[i] * nums[j]
                    if candidate > coins[i][j]:
                        coins[i][j] = candidate

        # def dfs(i: int, j: int) -> int:
        #     if coins[i][j] > -1:
        #         return coins[i][j]
        #     if i+1 == j:
        #         coins[i][j] = 0
        #         return coins[i][j]

        #     for k in range(i+1, j):
        #         left = dfs(i, k)
        #         right = dfs(k, j)
        #         coins[i][j] = max(coins[i][j], left + right + nums[k] * nums[i] * nums[j])
        #     return coins[i][j]

        # ret = dfs(0, len(nums)-1)
        return coins[0][len(nums)-1]


if __name__ == "__main__":
    print(Solution().maxCoins([1, 2, 0]))
    print(Solution().maxCoins([1, 5]))
    print(Solution().maxCoins([3, 1, 5, 8]))

