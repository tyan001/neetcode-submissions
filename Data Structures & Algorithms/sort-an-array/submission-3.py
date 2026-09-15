from collections import defaultdict
class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
       
        count = defaultdict(int)
        min_val, max_val = min(nums), max(nums)
        for num in nums:
            count[num] += 1

        lst = []

        for num in range(min_val,max_val+1):
            while count[num]>0:
                
                lst.append(num)
                count[num] -=1
        
        return lst