from typing import List


class Solution:

    def stoneGameVII(self, stones: List[int]) -> int:
        count = [[0 for _ in range(len(stones))] for _ in range(len(stones))]
