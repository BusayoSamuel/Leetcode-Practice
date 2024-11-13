"""
https://leetcode.com/problems/rotting-oranges/description/
"""

class Solution: #Time complexity O(nm), Space complexity O(nm)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if not (min(r + dr, c + dc) < 0 or r + dr >= ROWS
                    or c + dc >= COLS or grid[r+dr][c+dc] == 0):
                        if grid[r+dr][c+dc] == 1:
                            fresh -= 1
                            grid[r + dr][c + dc] = 2
                            q.append((r+dr, c+dc))


            time += 1


        return time if fresh == 0 else -1  

                
