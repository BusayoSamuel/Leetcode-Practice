"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/
"""

class Solution: #Time complexity O(E+V), Space complexity O(E+V)
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = collections.defaultdict(list)
        for src, dst in edges:
            incoming[dst].append(src)

        res = []
        for i in range(n):
            if not incoming[i]:
                res.append(i)
        return res
