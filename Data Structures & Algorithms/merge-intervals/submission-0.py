class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(1, n):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
            else:
                res.append(intervals[i-1])
        
        res.append(intervals[n-1])

        return res