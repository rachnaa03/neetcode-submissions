class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            summ = nums[left] + nums[right]
            if summ > target:
                right -= 1
            elif summ < target:
                left += 1
            else:
                return [left + 1, right + 1]