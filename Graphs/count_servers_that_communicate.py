"""
https://leetcode.com/problems/count-servers-that-communicate/description/
"""

class Solution: #Time complexity 0(mn), Space complexity O(m + n)
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and max(row_cnt[i], col_cnt[j]) > 1:
                    res += 1


        return res
        
