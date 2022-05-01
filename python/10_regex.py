class Solution:

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
    # print(Solution().isMatch('ab', 'ab'))
    # print(Solution().isMatch('ab', 'a.'))
    # print(Solution().isMatch('ab', '.*'))
    # print(Solution().isMatch('abc', '.*c'))
    # print(Solution().isMatch('a', 'ab*'))
    print(Solution().isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"))
    # print(Solution().isMatch('aaabaa', 'a*.a*'))
    # print(Solution().isMatch('baa', 'a*.a*'))
    # print(Solution().isMatch('aaa', 'ab*a*c*a'))
    # print(Solution().isMatch('abc', '.*abc'))
