from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        flag = [[True] * len(s) for i in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)):
                flag[i][j] = True if i >= j else flag[i+1][j-1] and s[i] == s[j]

        ans = {}

        def dfs(start: int, end: int) -> List[List[str]]:
            if ans.get((start, end)):
                return ans[start, end]
            if start > end:
                return None

            # ans[start, k-1] append s[k:end+1]
            for k in range(end, start-1, -1):
                if flag[k][end]:
                    prefixes = dfs(start, k-1)
                    cur_str = s[k:end+1]
                    if prefixes:
                        for prefix in prefixes:
                            copied = list(prefix)
                            copied.append(cur_str)
                            if ans.get((start, end)):
                                ans[start, end].append(copied)
                            else:
                                ans[start, end] = [copied]
                    else:
                        if ans.get((start, end)):
                            ans[start, end].append([cur_str])
                        else:
                            ans[start, end] = [[cur_str]]
            return ans[start, end]
        ret = dfs(0, len(s)-1)
        return ret


if __name__ == "__main__":
    print(Solution().partition("aabaab"))
