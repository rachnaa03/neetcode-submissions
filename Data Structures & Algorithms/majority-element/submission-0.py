class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        n = len(nums)
        majority = n // 2
        for num in nums:
            if freq[num] > majority:
                return num
        