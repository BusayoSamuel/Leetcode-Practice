"""
https://leetcode.com/problems/diameter-of-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            leftEdge = dfs(root.left)
            rightEdge = dfs(root.right)

            res = max(res, leftEdge + rightEdge)

            return max(leftEdge, rightEdge) + 1


        dfs(root)
        return res