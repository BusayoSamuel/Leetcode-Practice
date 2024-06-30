"""
https://leetcode.com/problems/pascals-triangle-ii/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(n^2) where n is the rowIndex
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[0,1,0]]
        
        while len(triangle) != rowIndex + 1:
            cur = [0]
            prev = triangle[-1]
            for i in range(len(prev)-1):
                cur.append(prev[i] + prev[i+1])
            cur.append(0)
            triangle.append(cur)

        return triangle[rowIndex][1:-1]

class CleanerSolution: #Same complexity
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]

        for i in range(rowIndex):
            nextRow = [0] * (i + 2)
            prevRow = triangle[-1]
            for j in range(len(prevRow)):
                nextRow[j] += prevRow[j]
                nextRow[j+1] += prevRow[j]
            triangle.append(nextRow)

        return triangle[rowIndex]

class CleanestSolution: #Time complexity O(n^2), Space complexity O(n) where n is the rowIndex
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            nextRow = [0] * (len(res) + 1)
            for j in range(len(res)):
                nextRow[j] += res[j]
                nextRow[j+1] += res[j]
            res = nextRow

        return res


