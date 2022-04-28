from typing import List

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        flag = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i + 1 >= len(word):
                    if s[i+1-len(word):i+1] == word:
                        flag[i] = flag[i-len(word)] if i-len(word) >= 0 else True
                        if flag[i]:
                            break
        return flag[len(s)-1]

if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
    print(Solution().wordBreak("applepenapple", ["apple", "pen", "epen"]))
