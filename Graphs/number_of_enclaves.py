"""
https://leetcode.com/problems/number-of-enclaves/description/
"""

class MySolution: #Time complexity O(m*n), Space complexity O(m*n) where m is number of rows and n is number of columns
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        res = 0
        visited = set()

        def dfs(r, c):
            nonlocal count 

            if min(r,c) < 0 or r >= ROWS or c  >= COLS:
                return False

            if grid[r][c] == 0:
                return True

            if (r, c) not in visited:
                count += 1
                visited.add((r, c))
            else:
                return True

            down = dfs(r+1, c)
            up = dfs(r-1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)

            return down and up and right and left


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and dfs(r, c):
                    res += count
                
                count = 0

        return res


class Solution: #Same complexity as above
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Return num of land cells
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                not grid[r][c] or (r, c) in visit):
                return 0
            visit.add((r, c))
            res = 1
            for dr, dc in direct:
                res += dfs(r + dr, c + dc)
            return res

        visit = set()
        land, borderLand = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] and (r, c) not in visit and
                    (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                    borderLand += dfs(r, c)

        return land - borderLand





        


        
