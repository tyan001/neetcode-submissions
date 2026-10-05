from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        

        seen = defaultdict(int)

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seen:
                return [seen[remain], i]
            
            seen[nums[i]] = i
        


    
