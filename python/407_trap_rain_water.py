from typing import List


class Solution:
    class Around(object):

        def __init__(self):
            self.left = 0
            self.right = 0
            self.up = 0
            self.down = 0

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        arounds = [[Solution.Around() for _ in range(len(heightMap[0]))] for _ in range(len(heightMap))]

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                arounds[i][j].left = max(heightMap[i][j-1], arounds[i][j-1].left) if j-1 >= 0 else 0
            for j in range(len(heightMap[0])-1, -1, -1):
                arounds[i][j].right = max(heightMap[i][j+1], arounds[i][j+1].right) if j+1 < len(heightMap[0]) else 0

        for j in range(len(heightMap[0])):
            for i in range(len(heightMap)):
                arounds[i][j].up = max(heightMap[i-1][j], arounds[i-1][j].up) if i-1 >= 0 else 0
            for i in range(len(heightMap)-1, -1, -1):
                arounds[i][j].down = max(heightMap[i+1][j], arounds[i+1][j].down) if i+1 < len(heightMap) else 0

        count = 0
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                around = arounds[i][j]
                min_height = min(around.left, around.right, around.up, around.down)
                if min_height > heightMap[i][j]:
                    count = count + min_height - heightMap[i][j]
        return count


if __name__ == "__main__":
    print(Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
    print(Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
    # fail case, you need dfs or bfs to fill all position
    print(Solution().trapRainWater([
        [12,13,1,12],
        [13,4,13,12],
        [13,8,10,12],
        [12,13,12,12],
        [13,13,13,13]]
))
