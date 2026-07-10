class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        n = len(nums)

        if n == 0 :
            return 0
        
        count = 1
        longest = 1
        
        for i in range(1, n):
            diff = nums[i] - nums[i-1]

            if diff == 1:
                count += 1
            elif diff == 0:
                continue
            else:
                count = 1
        
            longest = max(longest, count)
        
        return longest