"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(1)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None #start with prev
        res = float("inf")

        def dfs(node): #an in order traversal goes through the list in order
            nonlocal prev, res #allows you reference a variable within the scope of an outer function, you only use global for variables outside any function

            if not node:
                return

            dfs(node.left)
            if prev: #if prev is None
                res = min(res, abs(node.val - prev.val)) #compare the difference between nearest nodes
            prev = node
            dfs(node.right)


        dfs(root)

        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Same complexity as above
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        prev = None

        def dfs(node):
            nonlocal res
            nonlocal prev

            if not node:
                return

            dfs(node.left)
            if prev != None:
                res = min(res, abs(node.val - prev))
            prev = node.val
            dfs(node.right)

        dfs(root)
        return res
        

        
