from typing import List


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        f = [[None for _ in range(64)] for _ in range(len(piles))]

        def find_ans(i: int, m: int) -> (int, int):
            if i >= len(piles):
                return 0, 0

            if f[i][m] is not None:
                return f[i][m][0], f[i][m][1]

            f[i][m] = [0, 0]
            total = 0
            for x in range(1, 2*m + 1):
                if (i+x) > len(piles):
                    break
                total += piles[i+x-1]

                fir, sec = find_ans(i+x, max(m, x))
                if f[i][m][0] < sec + total:
                    f[i][m][0] = sec + total
                    f[i][m][1] = fir
            return f[i][m][0], f[i][m][1]

        ret = find_ans(0, 1)
        return ret[0]


if __name__ == "__main__":
    # print(Solution().stoneGameII(([1])))
    print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))
