"""
https://leetcode.com/problems/leaf-similar-trees/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n+m), Space complexity O(n+m) where n is the size of root1 and m is the size of root2 
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node.right and not node.left:
                leaves.append(node.val)
                return

            if node.left:
                dfs(node.left, leaves)

            if node.right:
                dfs(node.right, leaves)

        leaves1 = []
        leaves2 = []
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2



        
