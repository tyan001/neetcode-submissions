from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = defaultdict(int)

        for num in nums:
            hash_set[num] += 1
        
        for key,val in hash_set.items():
            if val == 1:
                ans = key
        
        return ans