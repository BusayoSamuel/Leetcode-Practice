"""
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity(n)
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def helper(node):
            nonlocal res

            if not node:
                return (0, 0)

            leftsum, leftcount = helper(node.left)
            rightsum, rightcount = helper(node.right)

            total = node.val + leftsum + rightsum
            count = 1+leftcount+rightcount

            if (total)//(count) == node.val:
                res += 1

            return (total, count)

        helper(root)
        return res

