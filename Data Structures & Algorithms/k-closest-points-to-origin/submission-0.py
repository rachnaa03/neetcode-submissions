import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        dist = 0 
        points_dist = []
        res = []

        for i in range(n):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            points_dist.append((dist, points[i]))
        
        points_dist.sort()

        for dist, point in points_dist[:k]:
            res.append(point)

        return res
