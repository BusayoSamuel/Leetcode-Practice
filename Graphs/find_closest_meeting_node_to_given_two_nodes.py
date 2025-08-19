"""
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        adj = defaultdict(list)
        for i, nei in enumerate(edges):
            adj[i].append(nei)

        def bfs(src, distMap):
            q = deque([(src, 0)])
            distMap[src] = 0
            while q:
                node, dist = q.popleft()
                for nei in adj[node]:
                    if nei not in distMap:
                        q.append((nei, dist + 1))
                        distMap[nei] = dist + 1

        node1Dist, node2Dist = {}, {}
        bfs(node1, node1Dist)
        bfs(node2, node2Dist)

        res, resDist = -1, float("inf")
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                dist = max(node1Dist[i], node2Dist[i])
                if dist < resDist:
                    resDist, res = dist, i

        return res
