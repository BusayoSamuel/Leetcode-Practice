"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, curVal):
            nonlocal res

            if not root:
                return

            curVal.append(str(root.val))

            if not root.left and not root.right:
                res += int("".join(curVal))
                curVal.pop()
                return

            dfs(root.left, curVal)
            dfs(root.right, curVal)
            curVal.pop()

        dfs(root, [])
        return res


class CleanerSolution: #Same complexity
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, num):

            if not node:
                return 0

            num = num * 10 + node.val

            if not node.left and not node.right:
                return num

            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)
