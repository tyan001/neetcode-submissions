from collections import defaultdict
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
        count = defaultdict(int)
        min_val, max_val = min(nums), max(nums)
        for num in nums:
            count[num] += 1

        lst = []

        for num in range(min_val,max_val+1):
            if count[num] > 0:
                temp = [num] * count[num]
                lst.extend(temp)
        
        return lst