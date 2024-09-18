"""
https://leetcode.com/problems/all-possible-full-binary-trees/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity, Space complexity O(2^n)
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = { 0 : [], 1 : [ TreeNode() ] } #This is essentially to prevent repeat calculation, this serves as a cache

        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n):
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2)) #if either the leftTrees or rightTrees are empty then this code wouldn't run, this ensures that each node would either have 0 or 2 child nodes
            dp[n] = res
            return res
        
        return backtrack(n)
