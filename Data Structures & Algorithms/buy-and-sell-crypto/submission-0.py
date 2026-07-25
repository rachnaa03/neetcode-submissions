class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        mini = prices[0]
        n = len(prices)

        for i in range(1, n):
            cost = prices[i] - mini
            profit = max(cost, profit)
            mini = min(prices[i], mini)
        
        return profit