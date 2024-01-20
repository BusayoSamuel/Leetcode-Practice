"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(logn) , Space complexity O(logn) because it's a BST
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(curNode):
            if not curNode:
                return TreeNode(val)

            if val > curNode.val:
                if not curNode.right:
                    curNode.right = TreeNode(val)
                else:
                    insert(curNode.right)
            else:
                if not curNode.left:
                    curNode.left = TreeNode(val)
                else:
                    insert(curNode.left)

            return curNode


        return insert(root)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SimplerSolution: #Same time complexity
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
