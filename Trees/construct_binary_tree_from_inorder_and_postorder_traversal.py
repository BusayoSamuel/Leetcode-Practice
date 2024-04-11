"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n^2), Space complexity O(n)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        root = TreeNode(postorder.pop())

        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root
    
class OptimalSolution: #Time complexity O(n), Space complexity O(n)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}

        def helper(l, r):
            if l > r: #important to have l > r not l == r
                return None
            
            root = TreeNode(postorder.pop())

            i = idx[root.val]
            root.right = helper(i+1, r)
            root.left = helper(l,i-1) #important to have i-1 here not i
            return root

        return helper(0, len(inorder)-1)