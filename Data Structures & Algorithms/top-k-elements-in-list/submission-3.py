class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeats = {}
        lst = []
        for num in nums:
            repeats[num] = repeats.get(num,0) + 1
        
        for key,val in repeats.items():
            lst.append([val,key])
        
        lst.sort()
        result = []

        for i in range(k):
            result.append(lst.pop()[1])
        
        return result
        
