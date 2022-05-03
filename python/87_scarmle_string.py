from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = dict()

        @cache      # use cache instead of memo, if we don't use cache, we will get a timeout, even we use lru_cache
        def match(i_s1: int, j_s1: int, i_s2: int, j_s2: int) -> bool:
            if memo.get((i_s1, j_s1, i_s2, j_s2)):
                return memo[(i_s1, j_s1, i_s2, j_s2)]

            if s1[i_s1: j_s1+1] == s2[i_s2: j_s2+1]:
                memo[(i_s1, j_s1, i_s2, j_s2)] = True
                return True

            if j_s1 - i_s1 <= 0:
                return False

            if sorted(s1[i_s1: j_s1+1]) != sorted(s2[i_s2: j_s2+1]):
                return False

            m = False
            for i in range(0, j_s1 - i_s1):
                # not exchange or exchange
                m = (match(i_s1, i_s1 + i, i_s2, i_s2 + i) and match(i_s1 + i + 1, j_s1, i_s2 + i + 1, j_s2)) \
                    or (match(i_s1, i_s1 + i, j_s2 - i, j_s2) and match(i_s1 + i + 1, j_s1, i_s2, j_s2 - i - 1))
                if m:
                    break
            memo[(i_s1, j_s1, i_s2, j_s2)] = m
            return m
        match.cache_clear()
        return match(0, len(s1)-1, 0, len(s2)-1)


if __name__ == "__main__":
    print(Solution().isScramble('abb', 'bba'))
    # i = 1
    # (0, 1, 0, 1) and (2, 4, 2, 4)
    # (0, 1, 3, 4) and (2, 4, 0, 2)
    # great eatrg
    print(Solution().isScramble('great', 'rgeat'))
    print(Solution().isScramble('abcde', 'caebd'))
    print(Solution().isScramble('a', 'a'))
