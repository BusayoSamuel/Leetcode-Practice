"""
https://leetcode.com/problems/count-the-number-of-complete-components/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v, res):
            if v in visit:
                return

            visit.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei, res)

            return res

        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        res = 0
        visit = set()

        for v in range(n):
            if v in visit:
                continue

            component = dfs(v, [])
            if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
                res += 1

        return res
        


        


        
