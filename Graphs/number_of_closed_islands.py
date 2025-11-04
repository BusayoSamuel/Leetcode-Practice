"""
https://leetcode.com/problems/number-of-closed-islands/description/
"""

class Solution: #Time complexity O(m * n), Space complexity O(m * n) where m is the number of rows and n is the number of columns
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(i, j):
            if min(i, j) < 0 or i >= ROWS or j >= COLS:
                return False

            if grid[i][j] == 1 or (i, j) in visited:
                return True

            visited.add((i, j))
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j+1)
            right = dfs(i, j-1)

            return up and down and left and right

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and (i, j) not in visited and dfs(i, j):
                    res += 1

        return res


class Solution: #Same complexity as above
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return 0  # False
            if grid[r][c] == 1 or (r, c) in visit:
                return 1  # True

            visit.add((r, c))
            res = True
            for dx, dy in directions:
                if not dfs(r + dx, c + dy):
                    res = False
            return res

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r, c) not in visit:
                    res += dfs(r, c)

        return res

        
