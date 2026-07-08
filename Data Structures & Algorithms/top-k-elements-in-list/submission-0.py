class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        ans = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        while k > 0:
            max_key = max(freq, key = freq.get)
            ans.append(max_key)
            del freq[max_key]
            k -= 1

        return ans