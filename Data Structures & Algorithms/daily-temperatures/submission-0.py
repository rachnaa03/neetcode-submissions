class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = []

        for i in range(n):
            ans = 0
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    ans = j - i
                    break
            res.append(ans)

        return res