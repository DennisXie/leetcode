from typing import List


class Solution:

    def stoneGameVII(self, stones: List[int]) -> int:
        count = [[0 for _ in range(len(stones))] for _ in range(len(stones))]
        f = [[None for _ in range(len(stones))]for _ in range(len(stones))]
        for i in range(len(stones)):
            f[i][i] = (0, 0)
            for j in range(i, len(stones)):
                count[i][j] = count[i][j-1] + stones[i] if j-1 >= i else stones[i]
        ops = []

        def dfs2(i: int, j: int, alice: bool) -> (int, int):
            if f[i][j] is not None:
                return f[i][j]
            if j - i == 1:
                m = max(stones[i], stones[j])
                f[i][j] = (m, 0) if alice else (0, m)
                return f[i][j][0], f[i][j][1]

            left = count[i][j - 1]
            right = count[i + 1][j]
            alice1, bob1 = dfs2(i, j - 1, not alice)
            alice2, bob2 = dfs2(i + 1, j, not alice)
            if alice:
                print(i, j, alice, alice1, bob1, alice2, bob2, left, right)
                if alice1 + left - bob1 > alice2 + right -bob2:
                    print(j, "choosed")
                    f[i][j] = (alice1 + left, bob1)
                    ops.append((i, j, j, alice))
                else:
                    print(i, "choosed")
                    f[i][j] = (alice2 + right, bob2)
                    ops.append((i, j, i, alice))
            else:
                print(i, j, alice, alice1, bob1, alice2, bob2, left, right)
                # if sec1 + left - fir1 < sec2 + right - fir2:
                if alice1 - (bob1 + left) < alice2 - (bob2 + right):
                    print(j, "choosed")
                    f[i][j] = (alice1, bob1 + left)
                    ops.append((i, j, j, alice))
                else:
                    print(i, "choosed")
                    f[i][j] = (alice2, bob2 + right)
                    ops.append((i, j, i, alice))

            return f[i][j][0], f[i][j][1]

        ret = dfs2(0, len(stones)-1, True)
        for i in f:
            print(i)
        ops.reverse()
        print(ops)
        print(ret[0], ret[1])
        return ret[0] - ret[1]


if __name__ == "__main__":
    print(Solution().stoneGameVII([5, 3, 1, 4, 2]))
