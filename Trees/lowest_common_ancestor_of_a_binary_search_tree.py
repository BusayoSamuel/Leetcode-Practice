"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #Time complexity O(logn), Space complexity 0(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curNode = root

        while curNode:
            if p.val < curNode.val and q.val < curNode.val:
                curNode = curNode.left
            elif p.val > curNode.val and q.val > curNode.val:
                curNode = curNode.right
            else:
                return curNode
            
