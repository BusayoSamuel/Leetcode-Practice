"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
"""

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        adj = defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)

        res = 0
        def dfs(node, parent):
            nonlocal res
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    passengers += p
                    res += ceil(p / seats)
            return passengers + 1

        dfs(0, -1)
        return res
