class Solution:
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     ans = []
    #     for i in range(2):
    #         for j in range(len(nums)):
    #             ans.append(nums[j])
    #     return ans
    
    # def getConcatenation(self, nums: List[int]) -> List[int]:

    #     ans = nums
    #     ans = ans+nums
    #     return ans

    
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)

        for i,num in enumerate(nums):
            print(i,num)
            ans[i] = ans[i+n] = num

        return ans