class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        sum = 0 
        
        for idx, s in enumerate(jewels):
            sum += stones.count(s)
            
        return sum