"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time Complexity O(n), Space Complexity O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1