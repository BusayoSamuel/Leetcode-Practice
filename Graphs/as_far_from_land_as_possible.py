"""
https://leetcode.com/problems/as-far-from-land-as-possible/description/
"""

class MyInefficientSolution: #Time complexity O(n^4), Space complexity O(n^2)
    def maxDistance(self, grid: List[List[int]]) -> int:
        dxdy = [(0,1), (1,0), (-1, 0), (0, -1)]
        n = len(grid)
        res = -1
        def bfs(node):
            nonlocal res
            q = deque([node])
            visited = set()
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()

                    if min(x, y) < 0 or max(x, y) >= n or (x, y) in visited:
                        continue

                    if grid[x][y] == 1:
                        res = max(res, abs(node[0]-x) + abs(node[1]-y) )
                        return

                    visited.add((x,y))

                    for dx, dy in dxdy:
                        q.append(((x+dx), (y+dy)))



        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    bfs((r, c))


        return res


class Solution: #Time complexity O(n^2), Space complexity O(n^2)
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()

        #initialise the queue with land cells
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r, c])

        res = -1
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q:
            r, c = q.popleft()
            res = grid[r][c]

            for dr, dc in direct:
                newR, newC = r + dr, c + dc
                if min(newR, newC) >= 0 and max(newR, newC) < N and grid[newR][newC] == 0:
                    q.append([newR, newC])
                    grid[newR][newC] = grid[r][c] + 1 #update each cell visited with the shortest distance

        return res - 1 if res > 1 else -1 #if res == 1 that means that alls cells were land so need to return -1
        
