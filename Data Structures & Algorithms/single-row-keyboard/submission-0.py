class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        hash1 = {}
        for i in range(len(keyboard)):
            hash1[keyboard[i]] = i
        
        prev = 0
        total =0 
        for c in word:
            
            total += abs(prev - hash1[c])
            prev = hash1[c]
        
        return total