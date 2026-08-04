class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0

        negative = False
        if x < 0:
            negative = True
            x = -x

        while x:
            digit = x % 10
            x //= 10
            ans = ans * 10 + digit
                
        if not (-2**31< ans < 2**31 - 1): 
            return 0
        
        return -ans if negative else ans
        