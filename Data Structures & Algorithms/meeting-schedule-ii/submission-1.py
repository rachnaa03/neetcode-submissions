"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        n = len(intervals)

        if n == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        heap = []
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, n):
            if intervals[i].start < heap[0]:
                heapq.heappush(heap, intervals[i].end)
            
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
        
        return len(heap)