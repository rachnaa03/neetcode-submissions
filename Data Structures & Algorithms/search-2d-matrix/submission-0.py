def bs(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                col = bs(matrix[i], target)
                
                if col:
                    return True
        return False