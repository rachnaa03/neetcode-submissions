import math 

def min_hours(piles, speed):
    total = 0

    for pile in piles:
        total += math.ceil(pile/speed)

    return total

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            hours = min_hours(piles, mid)

            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low