class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        f = [[101] * len(s) for _ in range(2)]

        def cost(l: int, r: int):
            _cost = 0
            while l <= r:
                if s[l] != s[r]:
                    _cost += 1
                l += 1
                r -= 1
            return _cost

        for i in range(len(s)):
            f[0][i] = cost(0, i)

        i = 0
        # n=1 have been calculated before
        for n in range(2, k+1):
            i = 1 - i
            for j in range(n-1):
                f[i][j] = 0

            for j in range(n-1, len(s)):
                f[i][j] = 101   # avoid n - 2 memory
                for l in range(n-2, j):
                    f[i][j] = min(f[i][j], f[1-i][l] + cost(l+1, j))
        print(f, i)
        return f[i][len(s)-1]


if __name__ == "__main__":
    # print(Solution().palindromePartition("abab", 1))
    # print(Solution().palindromePartition("abab", 2))
    print(Solution().palindromePartition("ababa", 3))
