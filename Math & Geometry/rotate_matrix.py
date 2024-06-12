"""
https://leetcode.com/problems/rotate-image/description/
"""

class Solution: #Time complexity O(n^2), Space complexity O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r: #if l == r that means we've entered the center of the matrix, which doesn't change position
            for i in range(r - l): #we go through each layer of the matrix
                top, bottom = l, r

                #we swap cells in the anticlockwise direction
                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1



class MySolution: #Same complexity, different method of rotating cells
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0 
        r = len(matrix) - 1

        while l <= r:
            for i in range(r-l):
                top, bottom = l, r

                #we swap cells in the clockwise direction
                temp = matrix[top + i][r]
                matrix[top + i][r] = matrix[top][l + i]

                matrix[bottom][r - i], temp = temp, matrix[bottom][r - i]

                matrix[bottom - i][l], temp = temp, matrix[bottom - i][l]

                matrix[top][l + i] = temp

            l += 1
            r -= 1 
