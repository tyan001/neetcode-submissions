class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        self.heap_sort(nums)
    
    def heapify(self, arr:List[int],n: int,index:int) -> None:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]

            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)


    def heap_sort(self, arr: List[int]) -> None:
        n = len(arr)
        for i in range((n//2) - 1, -1, -1):
            self.heapify(arr,n,i)
    
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]

            # Heapify the reduced heap
            self.heapify(arr, i, 0)
