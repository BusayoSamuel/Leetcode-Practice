"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
"""

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)} #a mapping between each vertex and their neighbours

        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par) #covers cases where a child has multiple parents but you want to maintain a consistent path between them

        def dfs(node, par):
            time = 0

            for child in adj[node]:
                if child == par:
                    continue
                childTime = dfs(child, node) # we check the time it takes to travel to each child
                if childTime or hasApple[child]: #if the direct child has an apple or a descendant child has an apple we count time is takes to go down and up the tree
                    time += 2 + childTime

            return time


        return dfs(0, -1)