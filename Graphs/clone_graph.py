"""
https://leetcode.com/problems/clone-graph/description/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class MySolution: #Time complexity O(E+V), Space complexity O(E+V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {None: None}
        
        def dfs(node):
            if not node:
                return

            newNode = Node(node.val, [])
            hashmap[node] = newNode

            for n in node.neighbors:
                if n not in hashmap:
                    dfs(n)

                hashmap[node].neighbors.append(hashmap[n])


        dfs(node)
        return hashmap[node]

class Solution: #Time complexity O(E+V), Space complexity O(E+V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
        
