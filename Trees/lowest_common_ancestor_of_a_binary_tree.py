"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution: #Time complexity O(n), Space complexity O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res 

            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == p.val or node.val == q.val:
                if left or right:
                    res = node
                    return False
                else:
                    return True
            else:
                if left and right:
                    res = node
                    return False
                elif left or right:
                    return True
                else:
                    return False


        dfs(root)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #Same complexity as above
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def dfs(node):
            nonlocal lca
            if not node:
                return [False, False]
            if lca:
                return [False, False]

            left = dfs(node.left)
            right = dfs(node.right)
            res = [left[0] or right[0] or (node == p), left[1] or right[1] or (node == q)]
            if res[0] and res[1] and not lca:
                lca = node

            return res 

        dfs(root)
        return lca

                
        
