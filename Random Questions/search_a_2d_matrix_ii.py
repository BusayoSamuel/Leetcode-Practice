"""
https://leetcode.com/problems/search-a-2d-matrix-ii/description/
"""

class MySolution: #Time complexity O(mlogn), Space complexity O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (r+l)//2

                if arr[m] < target:
                    l = m + 1
                elif arr[m] > target:
                    r = m - 1
                else:
                    return True
            
            return False

        for i in range(len(matrix)):
            if binSearch(matrix[i]):
                return True

        return False
    

class Solution: #Time complexity O(m+n), Space complexity O(1) 
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #as all rows are sorted from left to right and columns sorted from top to bottom, we start from the bottom corner
        i = len(matrix) - 1
        j = 0

        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] > target: 
                i -= 1 #cells above the curr position would be lower in value
            elif matrix[i][j] < target:
                j += 1 #cells to the right of curr position would be higher in value
            else:
                return True 

        return False