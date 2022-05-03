from functools import lru_cache

class Solution:

    def isMatch2(self, s: str, p: str) -> bool:

        @lru_cache()
        def match(i: int, j: int) -> bool:
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False

            # if i >= len(s):
            #     if j+1 < len(p) and p[j+1] == '*':
            #         return match(i, j+2)
            #     else:
            #         return False

            if j+1 < len(p) and p[j+1] == '*':
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    return match(i+1, j) or match(i, j+2) or match(i+1, j+2)
                else:
                    return match(i, j+2)
            else:
                if i < len(s) and s[i] == p[j] or p[j] == '.':
                    return match(i+1, j+1)
                else:
                    return False
        return match(0, 0)

    def isMatch(self, s: str, p: str) -> bool:

        def match(i: int, j: int) -> bool:
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            # the last char of pattern string is * or sub string is .*.*.*
            if i >= len(s):
                if p[j] == '*':
                    return match(i, j+1)
                elif j < len(p) - 1 and p[j+1] == '*':
                    return match(i, j+2)
                else:
                    return False

            if p[j] == '.':
                f = match(i+1, j+1)
                if not f and j < len(p)-1 and p[j+1] == '*':
                    # for case 'abc' '.*abc'
                    return match(i, j+2)
                else:
                    return f
            elif p[j] == '*':
                if p[j-1] == '.':
                    return match(i+1, j+1) or match(i+1, j) or match(i, j+1)
                else:
                    # Do not care the last char is *
                    if s[i] == p[j-1]:
                        return match(i+1, j+1) or match(i+1, j) or match(i, j+1)
                    else:
                        return match(i, j+1)
            else:
                if s[i] == p[j]:
                    return match(i+1, j+1) or (j < len(p) - 1 and p[j+1] == '*' and match(i, j+2))
                elif j < len(p)-1 and p[j+1] == '*':
                    # for case 'baa' 'a*.a*'
                    return match(i, j+2)
                else:
                    return False

        return match(0, 0)


if __name__ == "__main__":
    print(Solution().isMatch2('ab', 'ab'))
    print(Solution().isMatch2('ab', 'a.'))
    print(Solution().isMatch2('ab', '.*'))
    print(Solution().isMatch2('abc', '.*c'))
    print(Solution().isMatch2('a', 'ab*'))
    print(Solution().isMatch2("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"))
    print(Solution().isMatch2('aaabaa', 'a*.a*'))
    print(Solution().isMatch2('baa', 'a*.a*'))
    print(Solution().isMatch2('aaa', 'ab*a*c*a'))
    print(Solution().isMatch2('abc', '.*abc'))
