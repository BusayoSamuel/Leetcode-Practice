"""
https://leetcode.com/problems/construct-quad-tree/description/
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class MySolution: #Time complexity O(n^2logn) - we make logn recursive calls (keep dividing by) and on each call we do an n^2 search, #Space complexity O(n^2logn)
    def construct(self, grid: List[List[int]]) -> 'Node':
        count = 0

        gridlen = len(grid[0])

        for i in range(gridlen):
            for j in range(gridlen):
                count += grid[i][j]

        if count == gridlen * gridlen:
            isLeaf = 1
            val = 1
        elif count == 0:
            isLeaf = 1
            val = 0
        else:
            isLeaf = 0
            val = None

        if isLeaf:
            return Node(val, isLeaf, None, None, None, None)

        #topleft
        topleft = []

        for i in range(gridlen//2):
            topleft.append(grid[i][:gridlen//2])

        #topright
        topright = []

        for i in range(gridlen//2):
            topright.append(grid[i][gridlen//2:])

        #bottomleft
        bottomleft = []

        for i in range(gridlen//2, gridlen):
            bottomleft.append(grid[i][:gridlen//2])

        #bottomright
        bottomright = []

        for i in range(gridlen//2, gridlen):
            bottomright.append(grid[i][gridlen//2:])

        return Node(val, isLeaf, self.construct(topleft), self.construct(topright), self.construct(bottomleft), self.construct(bottomright))
            

"""
# Definition for a QuadTree node.
class Node: 
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution: #Time complexity O(n^2logn) - we make logn recursive calls (keep dividing by) and on each call we do an n^2 search, #Space complexity O(logn)
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            
            if allSame:
                return Node(grid[r][c], True)

            n = n//2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)
        