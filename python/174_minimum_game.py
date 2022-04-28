from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        hp = [[(0, 0) for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        hp[0][0] = (-dungeon[0][0], -dungeon[0][0])
        for i in range(1, len(dungeon)):
            hp_left = hp[i-1][0][1]+dungeon[i][0]
            hp[i][0] = (min(hp[i-1][0][0], hp_left), hp_left)
        for j in range(1, len(dungeon[0])):
            hp_left = hp[0][j-1][1]+dungeon[0][j]
            hp[0][j] = (min(hp[0][j-1][0], hp_left), hp_left)

        for i in range(1, len(dungeon)):
            for j in range(1, len(dungeon[0])):
                hp_left1 = hp[i-1][j][1]+dungeon[i-1][j]
                minimum1 = min(hp[i-1][j][0], hp_left1)
                hp_left2 = hp[i][j-1][1]+dungeon[i][j-1]
                minimum2 = min(hp[i][j-1][0], hp_left2)
                if minimum1 > minimum2:
                    hp[i][j] = (minimum1, hp_left1)
                elif minimum1 < minimum2:
                    hp[i][j] = (minimum2, hp_left2)
                else:
                    hp[i][j] = (minimum1, hp_left1) if hp_left1 > hp_left2 else (minimum2, hp_left2)

        return 1 if hp[-1][-1][0] >= 0 else abs(hp[-1][-1][0]) + 1


if __name__ == "__main__":
    print(Solution().calculateMinimumHP(None))
