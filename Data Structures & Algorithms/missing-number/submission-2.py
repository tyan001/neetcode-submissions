from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hash1 = defaultdict(int)

        for num in nums:
            hash1[num] += 1
        
        for i in range(len(nums)+1):
            if i not in hash1:
                return i
