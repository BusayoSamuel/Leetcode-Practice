"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #O(n) time complexity, #O(n) space complexity
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            if not root:
                return

            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return res