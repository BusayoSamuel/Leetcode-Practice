"""
https://leetcode.com/problems/regions-cut-by-slashes/
"""


class Solution: #Time complexity O(n^2), Space complexity O(n ^ 2)
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS1, COLS1 = len(grid), len(grid[0])
        ROWS2, COLS2 = 3 * ROWS1, 3 * COLS1
        grid2 = [[''] * COLS2 for _ in range(ROWS2)]

        for row1 in range(ROWS1):
            for col1 in range(COLS1):
                r = row1 * 3
                c = col1 * 3

                if grid[row1][col1] == '/':
                    grid2[r][c+2] = 1
                    grid2[r+1][c+1] = 1
                    grid2[r+2][c] = 1
                elif grid[row1][col1] == '\\':
                    grid2[r][c] = 1
                    grid2[r+1][c+1] = 1
                    grid2[r+2][c+2] = 1
        
        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS2 or c >= COLS2 or (r, c) in visited or grid2[r][c] == 1:
                return

            visited.add((r,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)


        res = 0
        visited = set()
        for r in range(ROWS2):
            for c in range(COLS2):
                if (r,c) not in visited and grid2[r][c] == '':
                    dfs(r,c)
                    res += 1

        return res



