"""
https://leetcode.com/problems/same-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1: #Time complexity O(p + q), Space complexity O(p + q)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Consider all the base cases
        if not p and not q: #if both p and q are null
            return True

        if not p or not q: #if either p or q are null
            return False

        if q.val != p.val: #if the values of p and q are not the same
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

class Solution2: #Same complexity as above
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True

            if p and q:
                left = dfs(p.left, q.left) 
                right = dfs(p.right, q.right)
                return p.val == q.val and left and right 
            else:
                return False

        return dfs(p,q)


class MySolution: #Same complexity as above
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right):
                return True
            else:
                return False


        return dfs(p, q)
        
