import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        result = []
        for point in points:
            distance = math.sqrt((point[0]**2)+(point[1]**2))
            min_heap.append((distance, point[0], point[1]))
        
        heapq.heapify(min_heap)

        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            result.append([x,y])
        return result