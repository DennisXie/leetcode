from typing import List

class Solution:

    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        def make()->List[List[int]]:
            return [[0] * len(heightMap[0]) for _ in len(heightMap)]
        i_right_max = make()
        i_left_max = make()
        j_up_max = make()
        j_down_max = make()
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                i_left_max[i][j] = max(heightMap[i][j], i_left_max[i][j-1]) if j-1>=0 else 0
            for j in range(len(heightMap[0])-1, -1, -1):
                i_right_max[i][j] = max(heightMap[i][j], i_right_max[i][j+1]) if j+1<len(heightMap) else 0

        for j in range(len(heightMap[0])):
            for i in range(len(heightMap)):
                j_up_max[i][j] = max(heightMap[i][j], j_up_max[i-1][j]) if i-1>=0 else 0
            for j in range(len(heightMap)-1, -1, -1):
                j_down_max[i][j] = max(heightMap[i][j], j_down_max[i+1][j]) if i+1<len(heightMap[0]) else 0

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                pass


