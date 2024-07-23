"""
https://leetcode.com/problems/unique-paths/description/
"""

class MySolution: #Inefficient
    def uniquePaths(self, m: int, n: int) -> int:
        visited = set()
        res = 0

        def backtrack(i, j):
            nonlocal res
            
            if (i, j) in visited or i >= m or j >= n:
                return

            if i == m - 1 and j == n - 1:
                res += 1
                return

            visited.add((i, j))

            backtrack(i+1, j)

            backtrack(i, j + 1)

            visited.remove((i, j))

        backtrack(0, 0)
        return res

class EfficientSolution: #Time complexity O(mn), Space complexity O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


class MoreEfficientSolution: #Time complexity O(mn), Space complexity O(n)
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row = [1] * n
        prev_row = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                curr_row[j] = curr_row[j - 1] + prev_row[j]    
            curr_row, prev_row = prev_row, curr_row
        
        return prev_row[-1]
        
            
        
