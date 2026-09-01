class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)-1):
            maxRight=0
            for j in range(i+1,len(arr)):
                maxRight = max(maxRight, arr[j])
            arr[i] = maxRight

        arr[-1] = -1
        return arr 
