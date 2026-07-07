class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            cpl = target - nums[i]
            if cpl in seen:
                return [seen[cpl], i]
            seen[nums[i]] = i
