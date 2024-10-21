"""
https://leetcode.com/problems/trim-a-binary-search-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class OtherSolution: # Same complexity, probably makes the most sense
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high) #we can be sure that the left would be outside the limit, so we discard
        elif root.val > high:
            return self.trimBST(root.left, low, high) #we can be sure that the right would be outside the limit, so we discard

        root.left = self.trimBST(root.left, low, high) #then we perform a trim on the each branch 
        root.right = self.trimBST(root.right, low, high)

        return root



class MySolution: #Time complexity O(n), Space complexity O(n), not sure how this works though, just a different order of operations i guess
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val < low:
                if node.right: 
                    return node.right 
            elif node.val > high:
                if node.left:
                    return node.left
            else:
                return node

        return dfs(root)

class MyOtherSolution: # Same complexity
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val < low:
            if root.right:
                return root.right
        elif root.val > high:
            if root.left:
                return root.left
        else:
            return root







