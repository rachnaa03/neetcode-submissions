class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        count = 0

        prev = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                count += 1
                prev = min(prev, intervals[i][1])
        
        return count
