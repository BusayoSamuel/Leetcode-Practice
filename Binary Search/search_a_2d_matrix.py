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

#A bit cleaner
class Solution: #Same complexity
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        top = 0
        bottom = m - 1

        while top <= bottom:
            center = (top +  bottom)//2

            if target < matrix[center][0]:
                bottom = center - 1
            elif target <= matrix[center][-1]: # if target fails the first condition, then certainly target is > matrix[center][0]
                l = 0
                r = n - 1

                while l <= r:
                    mid = (r+l)//2

                    if target < matrix[center][mid]:
                        r = mid - 1
                    elif target > matrix[center][mid]:
                        l = mid + 1
                    else:
                        return True
                return False
            else:
                top = center + 1

        return False
