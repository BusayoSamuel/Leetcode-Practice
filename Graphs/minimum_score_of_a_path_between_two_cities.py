"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
"""

class Solution: #Time complexity O(V+E), Space complexity O(V+E)
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        res = float("inf")
        visit = set()

        def dfs(node):
            nonlocal res
            if node in visit:
                return
            visit.add(node)
            for nei, dist in adj[node]:
                res = min(res, dist)
                dfs(nei)

        dfs(1)
        return res
