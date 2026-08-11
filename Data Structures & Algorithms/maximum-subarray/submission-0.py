class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        summ = 0
        maxx = -1

        for i in range(n):
            summ += nums[i]
            maxx = max(maxx, summ)

            if summ < 0:
                summ = 0
            
        
        return maxx
