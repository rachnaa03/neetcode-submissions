class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        s = set(nums)
        
        if n == 0:
            return 0
        
        longest = 1
        count = 1

        for num in s:
            if num - 1 not in s:
                start = num
                count = 1

                while start + 1 in s:
                    count += 1
                    start += 1
                
                longest = max(longest, count)
        return longest
                
