from typing import List


class Solution:

    def findMaximizedCapital2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            profits.sort(reverse=True)
            return w + sum(profits[:k])

        capital_profits = []
        for i in range(len(profits)):
            capital_profits.append((capital[i], profits[i]))

        capital_profits.sort()
        candidates = list()
        last_j = 0
        for i in range(k):
            for j in range(last_j, len(capital_profits)):
                if w >= capital_profits[j][0]:
                    candidates.append(capital_profits[j][1])
                else:
                    candidates.sort(reverse=True)
                    break
            else:
                candidates.sort(reverse=True)
                j += 1
            last_j = j
            candidates = candidates[:k-i]
            if len(candidates) > 0:
                w += candidates.pop(0)
            else:
                break
        return w

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capital_profits = {}
        for i in range(len(profits)):
            if capital[i] in capital_profits:
                capital_profits[capital[i]].append(profits[i])
            else:
                capital_profits[capital[i]] = [profits[i]]

        capital_set = list(set(capital))
        capital_set.sort()

        for _, v in capital_profits.items():
            v.sort()

        for i in range(k):
            cur_max = 0
            cur_capital = None
            for c in capital_set:
                if c <= w and len(capital_profits[c]) > 0 and cur_max < capital_profits[c][-1]:
                    cur_max = capital_profits[c][-1]
                    cur_capital = c
            if cur_capital is not None:
                capital_profits[cur_capital].pop(-1)
                w += cur_max
            else:
                break
        return w


if __name__ == "__main__":
    # print(Solution().findMaximizedCapital2(30, 0, [1, 2, 3], [1, 1, 2]))
    print(Solution().findMaximizedCapital2(2, 0, [1, 2, 3], [0, 1, 1]))
