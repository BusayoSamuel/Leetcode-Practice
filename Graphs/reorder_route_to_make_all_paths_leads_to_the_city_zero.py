"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
"""


class Solution: #Time complexity O(n), Space comlexity O(n)
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal changes
            visit.add(city)
            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                if (neighbor, city) not in edges:
                    changes += 1
                dfs(neighbor)

        dfs(0)
        return changes
