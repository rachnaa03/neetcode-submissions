class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        left = 0
        last = {}
        ans = []
        n = len(s)

        for i in range(n):
            last[s[i]] = i

        while left < n:
            right = last[s[left]]

            for i in range(left, n):
                right = max(right, last[s[i]])

                if i == right:
                    ans.append(right - left + 1)
                    left = right + 1
                    break
        return ans