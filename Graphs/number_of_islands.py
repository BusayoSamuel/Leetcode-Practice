"""
https://leetcode.com/problems/number-of-islands/description/
"""
class MySolution: #Time complexity O(ROWS*COLS), Space complexity O((ROWS*COLS)
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        COLS = len(grid[0])
        ROWS = len(grid)

        def mapOut(i, j):
            if min(i, j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0" or (i, j) in visited:
                return

            visited.add((i,j))
            mapOut(i+1, j)
            mapOut(i-1, j) 
            mapOut(i, j+1)
            mapOut(i, j-1)


        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    mapOut(i,j)

        return res

        
