import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            else:
                if x > y:
                    x = x - y
                    heapq.heappush(stones,-x)
                else:
                    y = y - x
                    heapq.heappush(stones, -y)

        return -stones[0] if stones else 0