class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        

        map = {}
        
        for word in strs:
            freq = [0] * 26

            for ch in word:
                idx = ord(ch) - ord('a')
                freq[idx] += 1

            key = tuple(freq)

            if key not in map:
                map[key] = []
            
            map[key].append(word)

        return list(map.values())


                

            

