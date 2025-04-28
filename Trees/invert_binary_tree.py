"""
https://leetcode.com/problems/invert-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #O(n) time complexity, #O(n) space complexity
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

class MySolution: #Same complexity as above
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            tmp = node.left
            node.left = node.right
            node.right = tmp
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
