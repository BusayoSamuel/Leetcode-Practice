"""
https://leetcode.com/problems/subtree-of-another-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(root * subRoot), Space complexity O(root * subRoot)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subRoot:
            return True

        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Same complexity as above
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if self.isSameTree(root, subRoot):
            return True

        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2 or node1.val != node2.val:
                return False

            return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)

        

        
