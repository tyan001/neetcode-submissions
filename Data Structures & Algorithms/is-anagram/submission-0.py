class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp1 = sorted(s)
        temp2 = sorted(t)

        for i in range(len(temp1)):
            if temp1[i] != temp2[i]:
                return False

        return True