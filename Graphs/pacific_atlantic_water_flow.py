"""
https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/1470836687/
"""


class MySolution: #Time complexity O(nm) #Space complexity complexity O(nm)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        alt = set()

        def dfs(i, j, visit, prev):
            if (i,j) in visit or min(i,j) < 0 or i >= ROWS or j >= COLS or heights[i][j] < prev:
                return

            visit.add((i,j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, alt, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, alt, heights[r][COLS-1])


        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r, c) in alt:
                    res.append([r, c])


        return res
