class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])



        low = 0
        high = m * n - 1

        while low <= high:
            medium = (low+high) // 2
            i,j = medium//n, medium%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]<target:
                low = medium+1
            else:
                high = medium-1

        return False




        