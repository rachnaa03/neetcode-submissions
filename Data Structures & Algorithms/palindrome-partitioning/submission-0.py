class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        ans = []
        
        def isPal(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(ans.copy())
                return 
            
            for j in range(i, len(s)):
                if isPal(s, i, j):
                    ans.append(s[i:j+1])
                    backtrack(j + 1)
                    ans.pop()
                
        backtrack(0)
        return res