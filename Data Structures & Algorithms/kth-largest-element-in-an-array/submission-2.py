import heapq
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
        
    #     heapq.heapify(nums)

    #     while len(nums)>k:
    #         heapq.heappop(nums)
        
    #     return nums[0]
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)

        for i in range(k-1):
            heapq.heappop_max(nums)
        
        return nums[0]