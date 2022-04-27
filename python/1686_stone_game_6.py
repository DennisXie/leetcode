from typing import List


class Solution:

    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # note: assume we have [a1, a2] [b1, b2]
        # Alice will try to take the most different stone, that is a1-b2 > a2-b1 then 1 will be taken
        # or [52, 55] [58, 50] which one be taken by alice? (a1-b2) - (a2-b1) = (a1 + b1) - (a2 + b2)
        # now we can add alicevalues and bobvalues, and alice take the most valuable stone.
        total_values = [a + b for a, b in zip(aliceValues, bobValues)]
        total_values.sort(reverse=True)
        # [a0+b0, a2+b2, ..., a2k+b2k] - [b0, b1, ..., b2k] = [a0, a2, ..., a2k] - [b1, b3, ..., b2k-1]
        ans = sum(total_values[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0
