from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        
        biggest = float('-inf')
        for k,v in seen.items():
            if v > biggest:
                biggest = v
                majority_num = k
       
        return majority_num
            
        