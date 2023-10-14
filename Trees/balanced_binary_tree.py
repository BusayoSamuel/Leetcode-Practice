"""
https://leetcode.com/problems/balanced-binary-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return [True, 0] 

            left = dfs(root.left)
            right = dfs(root.right)
            bal = abs(left[1]-right[1]) <= 1 and left[0] and right[0] #Making sure the both the left and right children are also balanced
            return [bal, max(left[1], right[1]) + 1] #returning [if node is balanced, height of node]

        return dfs(root)[0]