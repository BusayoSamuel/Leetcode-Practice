"""
https://leetcode.com/problems/unique-paths-ii/description/
"""

class MySolution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rowN = len(obstacleGrid)
        colN = len(obstacleGrid[0])
        count = 0

        def backtrack(i, j):
            nonlocal count

            if obstacleGrid[i][j] == 1:
                return

            if i == rowN - 1 and j == colN - 1:
                count += 1
                return

            if i < rowN - 1:
                i += 1
                backtrack(i, j)
                i -= 1

            if j < colN - 1:
                j += 1
                backtrack(i, j)

        backtrack(0, 0)
        return count