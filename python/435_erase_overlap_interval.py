from typing import List


class Solution:

    def ereaseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return len(intervals) - self.maxUnoverlapedIntervals(intervals)

    def maxUnoverlapedIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = None
        count = 0
        for interval in intervals:
            if end is None or interval[0] >= end:
                count += 1
                end = interval[1]
        return count


if __name__ == "__main__":
    print(Solution().ereaseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(Solution().ereaseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
