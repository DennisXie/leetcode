from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        flag = [[True] * len(s) for i in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)):
                flag[i][j] = True if i >= j else flag[i+1][j-1]

        ans = []
        def dfs()
