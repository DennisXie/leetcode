from typing import List


class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        f = [None for _ in range(len(stoneValue))]

        def dfs(i: int) -> (int, int):
            if i >= len(stoneValue):
                return 0, 0

            if f[i] is not None:
                return f[i][0], f[i][1]

            f[i] = [-50000001, 0]
            count = 0
            for j in range(3):
                if i+j >= len(stoneValue):
                    break

                count += stoneValue[i+j]
                fir, sec = dfs(i+j+1)
                if sec + count > f[i][0]:
                    f[i][0] = sec + count
                    f[i][1] = fir
            return f[i][0], f[i][1]

        ret = dfs(0)
        if ret[0] > ret[1]:
            return "Alice"
        elif ret[0] < ret[1]:
            return "Bob"
        else:
            return "Tie"


if __name__ == "__main__":
    print(Solution().stoneGameIII([-1, -1, -3]))
