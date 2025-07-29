"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""

class MySolution: #Time complexity O(n * n), Space complexity O(n * n)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        q = deque()
        q.append((0,0))
        count = 0
        N = len(grid)
        visited = set()

        while q:
            count += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                if min(x, y) < 0 or x >=  N or y >= N or grid[x][y] == 1 or (x, y) in visited:
                    continue

                if x == N-1 and y == N-1:
                    return count

                for dx, dy in dirs:
                    q.append((x + dx, y + dy))

                visited.add((x,y))

        return -1


        


        
