class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        consecutive = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                counter = 0

            consecutive = max(counter, consecutive)
        return consecutive