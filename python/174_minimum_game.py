from typing import List


class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        hp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        hp[-1][-1] = 1 if 1 - dungeon[-1][-1] <= 0 else 1 - dungeon[-1][-1]
        for i in range(len(dungeon)-2, -1, -1):
            hp_left = hp[i+1][-1] - dungeon[i][-1]
            hp[i][-1] = 1 if hp_left <= 0 else hp_left
        for j in range(len(dungeon[0])-2, -1, -1):
            hp_left = hp[-1][j+1] - dungeon[-1][j]
            hp[-1][j] = 1 if hp_left <= 0 else hp_left

        for i in range(len(dungeon)-2, -1, -1):
            for j in range(len(dungeon[0])-2, -1, -1):
                hp_down = 1 if hp[i+1][j] - dungeon[i][j] <= 0 else hp[i+1][j] - dungeon[i][j]
                hp_right = 1 if hp[i][j+1] - dungeon[i][j] <= 0 else hp[i][j+1] - dungeon[i][j]
                hp[i][j] = min(hp_down, hp_right)
        return hp[0][0]


if __name__ == "__main__":
    print(Solution().calculateMinimumHP([
        [0, -2],
        [-1, 0]
    ]))
