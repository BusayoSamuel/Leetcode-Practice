"""
https://leetcode.com/problems/search-a-2d-matrix/description/
"""

class Solution: #Time complexity Olog(m*n), Space complexity O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1

        while u <= d:
            midRow = (u + d)//2
            if target > matrix[midRow][0] and target > matrix[midRow][-1]:
                u = midRow + 1
            elif target < matrix[midRow][0] and target < matrix[midRow][-1]:
                d = midRow - 1 
            else:
                while l <= r:
                    midCol = (l + r)//2
                    if target > matrix[midRow][midCol]:
                        l = midCol + 1
                    elif target < matrix[midRow][midCol]:
                        r = midCol - 1
                    else:
                        return True
                return False