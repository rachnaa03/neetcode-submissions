class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = right = 0
        maxlen = 0
        st = set()

        while right < len(s):
            
            if s[right] not in st:
                st.add(s[right])
                maxlen = max(maxlen, right - left + 1)
                right += 1
            else:
                st.remove(s[left])
                left += 1
        
        return maxlen