class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left, right = 0, n - 1
        maxx = 0

        while left < right:
            width = right - left
            area = min(heights[left], heights[right]) * width
            maxx = max(area, maxx)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxx