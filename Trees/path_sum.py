"""
https://leetcode.com/problems/path-sum/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, curSum):
            if not root:
                return False

            curSum += root.val
            if not root.left and not root.right:
                return curSum == targetSum

            return dfs(root.left, curSum) or dfs(root.right, curSum)

        return dfs(root,0)


class MySolution: #Same complexity as abovr
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur):
            if not node:
                return False

            if not node.left and not node.right:
                cur += node.val
                return cur == targetSum


            left = dfs(node.left, cur + node.val)
            right = dfs(node.right, cur + node.val)

            return left or right


        return dfs(root, 0)


        
