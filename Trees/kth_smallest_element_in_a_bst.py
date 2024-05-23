"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root):
            
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

            
        dfs(root)
        return res[k-1]
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BetterSolution: #Same complexity
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] #We keep track of nodes we will need to visit later
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val #We can stop immediately once we encountered kth element
            cur = cur.right

            

        