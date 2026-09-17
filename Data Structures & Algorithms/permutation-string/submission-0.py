class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):

            return False

        s1_hash = {}

        for c in s1:
            s1_hash[c] = s1_hash.get(c, 0) + 1
        
        s2_hash = {}
        start = end = 0
        window_size = len(s1)
        
        for end in range(len(s2)):
            
            s2_hash[s2[end]] = s2_hash.get(s2[end], 0) + 1

            if end - start + 1 == window_size:

                if s2_hash == s1_hash:
                    return True
                
                s2_hash[s2[start]] = s2_hash.get(s2[start]) - 1

                if s2_hash[s2[start]] == 0:
                    del s2_hash[s2[start]]
                
                start += 1

            
        return False
        