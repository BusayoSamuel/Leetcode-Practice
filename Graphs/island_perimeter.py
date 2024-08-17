"""
https://leetcode.com/problems/island-perimeter/description/
"""

class Solution: #Time complexity O(n*m), Space complexity O(n*m) where n is the number of rows and m is number of columns
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visited:
                return 0

            visited.add((i, j))
            
            perimeter = 0
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i - 1, j)
            perimeter += dfs(i, j + 1)
            perimeter += dfs(i, j - 1)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # Since there's only one island, we can return immediately after the first DFS call
                    return dfs(i, j)

        return 0  # Default return, though this line shouldn't be reached if the input is valid
