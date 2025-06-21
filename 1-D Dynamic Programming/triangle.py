"""
https://leetcode.com/problems/triangle/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(n^2) where n is the number of rows
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def dfs(i, j):
            if i >= len(triangle):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = triangle[i][j] + min(dfs(i+1, j), dfs(i+1, j+1))

            return dp[(i, j)]

        return dfs(0, 0)


class EfficientSolution: #Time complexity O(n^2), Space complexity O(n) where n is the number of rows
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(triangle[row]) for row in range(n)]
        dp[-1] = triangle[-1][:]
        
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[row][col] = triangle[row][col] + min(dp[row + 1][col], dp[row + 1][col + 1])

        return dp[0][0]
