class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        freq = {}

        for card in hand:
            freq[card] = freq.get(card, 0) + 1
        
        while freq:
            start = min(freq)

            for i in range(groupSize):
                if start not in freq:
                    return False
                
                freq[start] -= 1

                if freq[start] == 0:
                    del freq[start] 
                
                start += 1
        
        return True