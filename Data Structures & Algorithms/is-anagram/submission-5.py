class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        seen1 = {}
        seen2 = {}

        for char1, char2 in zip(s,t):
            seen1[char1] = seen1.get(char1,0) + 1
            seen2[char2] = seen2.get(char2,0) + 1

        
        return seen1 == seen2
        