class Solution:

    def minCut(self, s: str) -> int:
        flag = [[True] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)):
                if i >= j:
                    flag[i][j] = True
                else:
                    flag[i][j] = flag[i+1][j-1] and s[i] == s[j]

        f = [20002] * len(s)
        f[0] = 0
        for i in range(1, len(s)):
            if flag[0][i]:
                f[i] = 0
                continue

            for j in range(0, i):
                if flag[j+1][i]:
                    f[i] = min(f[i], f[j]+1)
        return f[len(s)-1]


if __name__ == "__main__":
    print(Solution().minCut("aabaa"))
