class Solution:
    def longestPalindrome(self, s: str) -> str:
        flag = [[False] * len(s) for _ in range(len(s))]
        longest = 1
        ans = s[0]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i >= j:
                    flag[i][j] = True
                else:
                    flag[i][j] = (flag[i+1][j-1] or i+1 >= j - 1) and s[i] == s[j]
                if flag[i][j] and j - i + 1 > longest:
                    longest = j - i + 1
                    ans = s[i:j+1]
        return ans


if __name__ == "__main__":
    print(Solution().longestPalindrome("cbbd"))
