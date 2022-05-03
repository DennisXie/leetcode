from typing import List

class Solution:

    def findRepeatedDnaSequence(self, s: str) -> List[str]:
        count = dict()
        L = 10
        for i in range(len(s) - L + 1):
            s2 = s[i: i+L]
            count[s2] = (count.get(s2) or 0) + 1

        r = list()
        for k, v in count.items():
            if v > 1:
                r.append(k)
        return r
