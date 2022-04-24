class Solution:

    def superEggDrop2(self, k: int, n: int) -> int:
        """superEggDrop实际上是能解的，只是O(kn^2)会超时，考虑到max_drop[k][n]在k固定是随n单调递增，故可以用二分查找
        二分查找涉及到前面的状态可能没有算出来，所以需要用记忆化搜索"""
        max_drop = [[None for i in range(n+1)] for j in range(k+1)]

        for i in range(n+1):
            max_drop[1][i] = i

        for i in range(k+1):
            max_drop[i][0] = 0

        def find_drop(i, j) -> int:
            if max_drop[i][j] is not None:
                return max_drop[i][j]

            low, high = 1, j
            while low <= high:
                mid = (low + high) // 2
                broken = find_drop(i-1, mid-1)
                safe = find_drop(i, j-mid)
                if broken > safe:
                    high = mid - 1
                    max_drop[i][j] = broken+1 if max_drop[i][j] is None else min(max_drop[i][j], broken + 1)
                else:
                    low = mid + 1
                    max_drop[i][j] = safe+1 if max_drop[i][j] is None else min(max_drop[i][j], safe + 1)
            return max_drop[i][j]

        return find_drop(k, n)

    def superEggDrop(self, k: int, n: int) -> int:
        max_drop = [[10002 for i in range(n+1)] for j in range(k+1)]

        for i in range(n+1):
            max_drop[1][i] = i

        for i in range(k+1):
            max_drop[i][0] = 0

        for i in range(2, k+1):
            for j in range(1, n+1):
                # 遍历前面的状态
                for m in range(1, j+1):
                    broken = max_drop[i-1][m-1] + 1
                    safe = max_drop[i][j-m] + 1
                    max_drop[i][j] = min(max_drop[i][j], max(broken, safe))
        return max_drop[k][n]


if __name__ == "__main__":
    print(Solution().superEggDrop2(4, 5000))
