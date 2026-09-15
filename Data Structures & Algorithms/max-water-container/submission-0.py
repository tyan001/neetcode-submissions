class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, max1 = 0, heights[0]
        r, max2 = len(heights)-1, heights[len(heights)-1]

        max_area = (r-l) * min(max1,max2)

        while l<r:
            area = (r-l) * min(heights[l],heights[r])
            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1
            
            max_area = max(max_area, area)
        
        return max_area
            
            