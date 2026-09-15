class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = 0

        for num in nums:
            val = num ^ val
        
        return val