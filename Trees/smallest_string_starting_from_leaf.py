"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n + (m * (h + logm))) where n is the number of nodes, m is number of leaf nodes and h is height of tree, Space complexity O(h + hm)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        heap = [] #O(hm) space
        curr = []

        def dfs(node):
            curr.append(chr(node.val + ord('a')))
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)

            if not node.left and not node.right:
                s = "".join(curr[::-1]) #O(h) time
                heapq.heappush(heap, s) #O(logm) time

            curr.pop()

        dfs(root)
        return heapq.heappop(heap)


class MyEffecientSolution: #Time complexity O(n + (m * (logm))) where n is the number of nodes, m is number of leaf nodes and h is height of tree, Space complexity O(h + hm)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        heap = []

        def dfs(node, curr): 

            curr = (chr(node.val + ord('a'))) + curr
            if node.left:
                dfs(node.left, curr)
            
            if node.right:
                dfs(node.right, curr)

            if not node.left and not node.right:
                heapq.heappush(heap, curr)

        dfs(root, "")
        return heapq.heappop(heap)


class TheEfficientSolution: #Time complexity O(n), Space complexity O(h)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node, curr):

            curr = (chr(node.val + ord('a'))) + curr
            
            if node.left and node.right:
                return min(dfs(node.left, curr), dfs(node.right, curr))

            if node.left:
                return dfs(node.left, curr)
            
            if node.right:
                return dfs(node.right, curr)

            return curr

        return dfs(root, "")

        

        

        
        
