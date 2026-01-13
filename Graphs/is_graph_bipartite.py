"""
https://neetcode.io/solutions/is-graph-bipartite
"""

class Solution: #Time complxeity O(n), Space complexity O(n)
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)  # Map node i -> odd=1, even=-1

        def bfs(i):
            if color[i]:
                return True
            q = deque([i])
            color[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if color[i] == color[nei]:
                        return False
                    elif not color[nei]:
                        q.append(nei)
                        color[nei] = -1 * color[i]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
