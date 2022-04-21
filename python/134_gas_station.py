from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        pos = []
        last = 0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            if last * d <= 0:
                diff.append(d)
                pos.append(i)
            else:
                diff[-1] += d
            last = d

        last = 0
        for i in range(len(diff)):
            if diff[i] > 0 and last <= 0:
                j = (i + 1) % len(diff)
                left = diff[i]
                while j != i:
                    left += diff[j]
                    j = (j + 1) % len(diff)
                    if left < 0:
                        break
                else:
                    return pos[i]
            elif diff[i] == 0 and len(diff) == 1:
                return 0
            last = diff[i]
        return -1


if __name__ == "__main__":
    gas = [1, 1, 1, 1, 1]
    cost = [0, 0, 0, 4, 1]
    print(Solution().canCompleteCircuit(gas, cost))
