"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return [0, 0]

            l_size, l_coins = dfs(node.left)
            r_size, r_coins = dfs(node.right)

            size = 1 + l_size + r_size
            coins = l_coins + r_coins + node.val

            extra = abs(size - coins)
            res += extra #the amount of extras indicates how many moves are necessary, doesnt matter if its positive or negative extras

            return [size, coins]

        dfs(root)
        return res
        
