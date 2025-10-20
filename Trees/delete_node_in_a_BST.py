"""
https://leetcode.com/problems/delete-node-in-a-bst/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        array = []
        m = -1

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if node.val != key: array.append(node)
            if node.val == root.val: m = len(array) - 1
            dfs(node.right)

        def struct(arr):
            l = 0 
            r = len(arr) - 1
            m = (r + l)//2
            print(m)
            
            if m < 0:
                return None

            curNode = arr[m]

            curNode.left = struct(arr[:m])
            curNode.right = struct(arr[m+1:])
            return curNode

        dfs(root)
        print(array)
        root = struct(array)
        return root


class Solution: #Time compleixty O(logn), Space compl;exity O(1)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: #replace with subtree on right
                return root.right
            elif not root.right: #replace with subtree on left
                return root.left
            else: #find largest possible value on left
                cur = root.left
                while cur.right:
                    cur = cur.right
                
                root.val = cur.val #replace ith largest value left
                root.left = self.deleteNode(root.left, root.val) #delete largest value from left subtree

        return root
