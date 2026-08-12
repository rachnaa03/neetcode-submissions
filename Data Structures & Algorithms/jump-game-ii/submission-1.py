class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        jumps = 0
        current = 0
        farthest = 0
        
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == current:
                jumps += 1
                current = farthest

        return jumps