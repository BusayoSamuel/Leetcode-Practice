"""
https://leetcode.com/problems/max-area-of-island/submissions/1431217296/
"""

class Solution: #Time complexity O(mn), Space complexity O(mn) where m, are the number of rows and columns
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def backtrack(i, j):
            if min(i, j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0 or (i,j) in visited:
                return 0

            visited.add((i,j)) #this prevents any double counting
            left = backtrack(i, j-1)
            right = backtrack(i, j+1)
            up = backtrack(i - 1, j)
            down = backtrack(i + 1, j)

            return 1 + left + right + up + down

        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, backtrack(i,j))

        return res

class OtherSolution: #Same complexity
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            if min(i, j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0 or (i,j) in visited:
                return 0

            visited.add((i,j))
            return 1 + dfs(i, j-1) + dfs(i, j+1) + dfs(i - 1, j) + dfs(i + 1, j)

        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, dfs(i,j))

        return res
        
        
