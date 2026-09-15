from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3
        for num in nums:
            bucket[num] += 1

        idx = 0
        for color, count in enumerate(bucket):
            for j in range(count):
                # print(f"{num}: {i}")
                nums[idx] = color
                idx+=1
        

        
  