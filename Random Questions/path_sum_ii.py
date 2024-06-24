"""
https://leetcode.com/problems/path-sum-ii/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n^2), Space complexity O(n^2) 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]: 

        res = []
        cur = []

        def dfs(root, targetSum):
            if not root:
                return

            if not root.left and not root.right:
                cur.append(root.val)
                targetSum -= root.val
                if targetSum == 0:
                    res.append(cur.copy()) #a copy of the cur list is made which takes O(n) time and O(n) space
                cur.pop()
                return

            cur.append(root.val)
            dfs(root.left, targetSum - root.val)
            dfs(root.right, targetSum - root.val)
            cur.pop()

            
        dfs(root, targetSum)
        return res

class CleanerSolution: #Same complexity
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]: 

        res = []
        cur = []

        def dfs(root, targetSum):
            if not root:
                return
            
            cur.append(root.val)
            if not root.left and not root.right:    
                if targetSum == root.val:
                    res.append(cur.copy())

            dfs(root.left, targetSum - root.val)
            dfs(root.right, targetSum - root.val)
            cur.pop()

            
        dfs(root, targetSum)
        return res
