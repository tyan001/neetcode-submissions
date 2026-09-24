from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq = defaultdict(int)
        left=right=0
        max_len = 0
        while right<len(s):

            freq[s[right]] +=1

            while freq[s[right]]>1:

                freq[s[left]]-=1
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left+=1
            
            max_len = max(max_len, right-left+1)
            right+=1
        
        return max_len