class Solution:

    def checkPartition(self, s: str) -> bool:
        flag = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i >= j:
                    flag[i][j] = True
                else:
                    flag[i][j] = (flag[i+1][j-1] or i+1 >= j-1) and s[i] == s[j]

        for i in range(0, len(s)-2):
            if not flag[0][i]:
                continue
            for j in range(i+1, len(s)-1):
                if flag[i+1][j] and flag[j+1][len(s)-1]:
                    return True
        return False


if __name__ == "__main__":
    print(Solution().checkPartition("abcbdd"))
    print(Solution().checkPartition("leetcode"))
    print(Solution().checkPartition("bcbddxy"))
    print(Solution().checkPartition("abbbdd"))
