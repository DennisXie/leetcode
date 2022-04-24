class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        longest = [[0 for i in range(len(s))] for j in range(len(s))]
        maximum = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if i == j:
                        longest[i][j] = 1
                    else:
                        longest[i][j] = longest[i+1][j-1] + 2
                else:
                    longest[i][j] = max(longest[i+1][j], longest[i][j-1])
                maximum = max(maximum, longest[i][j])
        # print(longest)
        return maximum


if __name__ == "__main__":
    print(Solution().longestPalindromeSubseq("abcddb"))
