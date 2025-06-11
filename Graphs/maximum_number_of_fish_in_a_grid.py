"""
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
"""

class MySolution: #Time complexity O(n*m), Space complexity 0(n*m) where n is the size of the rows and m is the size of the columns
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            left = dfs(r, c-1)
            right = dfs(r, c+1)
            up = dfs(r-1, c)
            down = dfs(r+1, c)

            return grid[r][c] + left + right + up + down

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visited:
                    res = max(res, dfs(r, c))

        return res


        
