"""
https://leetcode.com/problems/construct-string-from-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1: #Time complexity O(n), Space complexity O(n)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        if not root.left and not root.right:
            return str(root.val)

        right = "("+ str(self.tree2str(root.right)) + ")" if root.right else ""

        return str(root.val) + "(" + str(self.tree2str(root.left)) + ")"+ right
    
class Solution2: #Same time complexity but more efficient, string concatenation leads to O(n ^ 2)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            if not root:
                return ""

            res.append("(")
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")
            preorder(root.left)
            preorder(root.right)

            res.append(")")

        preorder(root)
        return "".join(res)[1:-1]

class MySolution: #Same time complexity with string concatenation
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if not left and not right:
            return str(root.val)
        elif left and not right:
            return str(root.val) + "(" + left + ")"
        else:
            return str(root.val) + "(" + left + ")" + "(" + right + ")"
