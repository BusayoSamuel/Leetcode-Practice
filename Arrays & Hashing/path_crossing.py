"""
https://leetcode.com/problems/path-crossing/submissions/1398258772/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        
        i = 0
        j = 0

        for p in path:
            
            if p == 'N':
                i += 1
            elif p == 'S':
                i -= 1
            elif p == 'E':
                j -= 1
            else:
                j += 1

            if (i, j) not in visited:
                visited.add((i, j))
            else:
                return True

        return False

        

class Solution: #Same complexity
    def isPathCrossing(self, path: str) -> bool:
        dir = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        visited = set()
        x, y = 0, 0

        for p in path:
            visited.add((x, y))
            dx, dy = dir[p]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                return True

        return False
