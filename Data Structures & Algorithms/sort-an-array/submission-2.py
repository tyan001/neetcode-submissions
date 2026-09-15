from collections import defaultdict
class Solution:
    def merge(self, arr1, arr2):

        res = [0] * (len(arr1) + len(arr2))
        i=0
        j=0
        m = len(arr1)
        n = len(arr2)
        idx=0
        while(i<m and j<n):
            if(arr1[i] < arr2[j]):
                res[idx] = arr1[i]
                idx+=1
                i+=1
            else:
                res[idx] = arr2[j]
                idx+=1
                j+=1

        while(i<m):
            res[idx] = arr1[i]
            idx+=1
            i+=1
        
        while(j<n):
            res[idx] = arr2[j]
            idx+=1
            j+=1

        return res

    def mergeSort(self, arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)
        

    def sortArray(self, nums: List[int]) -> List[int]:

        return self.mergeSort(nums)
        
    # def sortArray(self, nums: List[int]) -> List[int]:
       
    #     count = defaultdict(int)
    #     min_val, max_val = min(nums), max(nums)
    #     for num in nums:
    #         count[num] += 1

    #     lst = []

    #     for num in range(min_val,max_val+1):
    #         while count[num]>0:
                
    #             lst.append(num)
    #             count[num] -=1
        
    #     return lst