"""
https://leetcode.com/problems/find-eventual-safe-states/
"""

class Solution: #Time complexity O(E+V), Space complexity O(E+V)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return safe[node]
            safe[node] = True
            return safe[node]

        res = []
        for node in range(n):
            if dfs(node):
                res.append(node)
        return res
