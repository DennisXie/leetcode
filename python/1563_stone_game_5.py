from typing import List

class Solution:

    def stoneGame2(self, stoneValue: List[int]) -> int:
        score = [[None] * len(stoneValue) for _ in range(len(stoneValue))]
        for i in range(len(stoneValue)):
            score[i][i] = 0

        count = [[None] * len(stoneValue) for _ in range(len(stoneValue))]
        path = [[None] * len(stoneValue) for _ in range(len(stoneValue))]
        for i in range(len(stoneValue)):
            count[i][i] = stoneValue[i]
            for j in range(i + 1, len(stoneValue)):
                count[i][j] = count[i][j - 1] + stoneValue[j]
                path[i][j] = []


        def dfs(i: int, j: int) -> (int, List[int]):
            if score[i][j] is not None:
                return score[i][j], path[i][j]

            score[i][j] = 0

            for k in range(i, j):
                left, lp = dfs(i, k)
                right, rp = dfs(k+1, j)
                if count[i][k] > count[k+1][j]:
                    candidate = count[k+1][j] + right
                    candp = rp
                elif count[i][k] < count[k+1][j]:
                    candidate = count[i][k] + left
                    candp = lp
                else:
                    candidate = count[i][k] + max(left, right)
                    candp = lp if left > right else rp
                if score[i][j] < candidate:
                    score[i][j] = candidate
                    path[i][j] = list(candp or [])
                    path[i][j].append(k)

                score[i][j] = max(score[i][j], candidate)
            return score[i][j], path[i][j]

        ret, p = dfs(0, len(stoneValue) - 1)
        [print(s) for s in score]
        print(p)
        return ret

    def stoneGame(self, stoneValue: List[int]) -> int:
        score = [[None] * len(stoneValue) for _ in range(len(stoneValue))]
        for i in range(len(stoneValue)):
            score[i][i] = 0

        def dfs(i: int, j: int) -> int:
            if score[i][j] is not None:
                return score[i][j]

            score[i][j] = 0

            total = sum(stoneValue[i:j+1])
            suml = 0
            for k in range(i, j):
                suml += stoneValue[k]
                sumr = total - suml
                if suml > sumr:
                    right = dfs(k + 1, j)
                    candidate = sumr + right
                elif suml < sumr:
                    left = dfs(i, k)
                    candidate = suml + left
                else:
                    left = dfs(i, k)
                    right = dfs(k + 1, j)
                    candidate = suml + max(left, right)
                score[i][j] = max(score[i][j], candidate)
            return score[i][j]

        ret = dfs(0, len(stoneValue) - 1)
        return ret


if __name__ == "__main__":
    print(Solution().stoneGame([98, 77, 24, 49, 6, 12, 2, 44, 51, 96]))
    # print(Solution().stoneGame2([98, 77, 24, 49, 6, 12, 2, 44, 51, 96]))
