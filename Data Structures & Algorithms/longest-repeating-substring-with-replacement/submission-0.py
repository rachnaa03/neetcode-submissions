class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        maxfreq = maxlen = 0
        left = right = 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxfreq = max(maxfreq, freq[s[right]])
            window_size = right - left + 1

            if window_size - maxfreq > k:
                freq[s[left]] -= 1
                left += 1
            
            maxlen = max(maxlen, right - left + 1)
            right += 1

        return maxlen