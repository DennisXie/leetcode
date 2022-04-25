from typing import List


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        """
        explanation:
        f[i][j][0] represents in the piles of i to j, how many stones can the first people get
        f[i][j][1] represents in the piles of i to j, how many stones can the second people get
        so, for any f[i][j]
        f[i][j][0] = f[i+1][j][1] + piles[i], f[i][j][1] = f[i+1][j][0]
        or
        f[i][j][0] = f[i][j-1][1] + piles[j], f[i][j][1] = f[i][j-1][0]
        Because the two person are very smart, so every time the first people will choose the right
        previous state to let him has the maximum stones in current state. The second people in the
        current state will have no choice but accept. After choosing, the first people will be the
        second people and the second people will be the first pople in the next state. So, the first
        people in current state will have no choice in next state.
        :param piles:
        :return:
        """
        f = [[None for _ in range(len(piles))] for _ in range(len(piles))]
        for i in range(len(piles)):
            f[i][i] = [piles[i], 0]

        # 本题用递推的动态规划不是很好写，用记忆化搜索比较简单。递推写法需要斜着推出dp_table，以保证前面的状态已经计算出来。
        def find_ans(i: int, j: int) -> (int, int):
            if f[i][j] is not None:
                return f[i][j][0], f[i][j][1]

            fir, sec = find_ans(i, j-1)
            f[i][j] = [sec + piles[j], fir]

            fir, sec = find_ans(i+1, j)
            # first people choose the beneficial previous state, the second people have no choice.
            if sec + piles[i] > f[i][j][0]:
                f[i][j][0] = sec + piles[i]
                f[i][j][1] = fir

            return f[i][j][0], f[i][j][1]

        ret = find_ans(0, len(piles) - 1)
        # for i in range(len(f)):
        #     print(f[i])
        return ret[1] < ret[0]


if __name__ == "__main__":
    print(Solution().stoneGame([5, 3, 4, 5]))
    print(Solution().stoneGame([3, 7, 2, 3]))
