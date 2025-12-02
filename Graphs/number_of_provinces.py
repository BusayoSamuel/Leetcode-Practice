"""
https://leetcode.com/problems/number-of-provinces/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res = 0

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res
