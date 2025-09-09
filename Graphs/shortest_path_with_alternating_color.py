"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
"""

class Solution: #Time complexity O(V+E), Space complexity O(V+E)
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for a, b in redEdges:
            red[a].append(b)

        for u, v in blueEdges:
            blue[u].append(v)


        q = deque([[0, 0, None]])
        visit = set((0, None))
        res = [-1 for _ in range(n)]

        while q:
            node, length, prevEdgeColor = q.popleft()

            if res[node] == -1:
                res[node] = length

            if prevEdgeColor != 'RED':
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, 'RED'))
                        q.append([nei, length+1, 'RED'])

            if prevEdgeColor != 'BLUE':
                for nei in blue[node]:
                    if (nei, 'BLUE') not in visit:
                        visit.add((nei, 'BLUE'))
                        q.append([nei, length+1, 'BLUE'])

        return res
        
