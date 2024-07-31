"""
https://leetcode.com/problems/house-robber-iii/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0] #[withRoot, withoutRoot]

            if not node.left and not node.right:
                return [node.val, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            withRoot = node.val + left[1] + right[1]
            withoutRoot = max(left) + max(right) #very key, you want to consider the possibility that skipping the left or right node could generate a higher value as well
            return [withRoot, withoutRoot]


        return max(dfs(root))
