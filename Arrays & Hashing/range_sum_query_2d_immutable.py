"""
https://leetcode.com/problems/range-sum-query-2d-immutable/description/
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]): #Time complexity O(n^2), Space complexity O(n^2)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.sumMap = [[0] * (COLS + 1) for i in range(ROWS + 1)] #add a top and left layer of zeros to the original array to aid in calculation of prefix sums

        for r in range(ROWS):
            prefix = 0 #prefix sum is calculated and tagged to the bottom right corner of every sub matrix
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMap[r][c+1] #we add the prefix sum of the matrix above this row
                self.sumMap[r+1][c+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: #Time complexity O(1), Space complexity O(1)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 #we adjust the indexes to match their position on prefixsumMap

        bottomRight = self.sumMap[row2][col2]
        top = self.sumMap[row1-1][col2]
        left = self.sumMap[row2][col1-1]
        topLeft = self.sumMap[row1-1][col1-1]
        res = bottomRight - top - left + topLeft #topLeft sum is added back to counter the double subtraction

        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
