"""
https://leetcode.com/problems/pascals-triangle/description/
"""

class Solution: #Time complexity O(n^2) , Space complexity O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows >= 1:
            res.append([1])

        if numRows >= 2:
            res.append([1, 1])
        
        if numRows > 2:
            for i in range(2, numRows):
                numRow = [1, 1]
                for j in range(1, len(res[-1])):
                    numRow.insert(-1, res[-1][j] + res[-1][j-1])
                res.append(numRow)

        return res
