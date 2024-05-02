"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxVal):
            nonlocal count

            if not node:
                return

            if node.val >= maxVal:
                count += 1

            maxVal =  max(node.val, maxVal)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)

        return count
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class OtherSolution: #Same complexity
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
