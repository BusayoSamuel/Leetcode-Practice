"""
https://leetcode.com/problems/convert-bst-to-greater-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class MySolution: #Time complexity O(n), Space complexity O(n)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        nums = []
        
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfs(root)
        hashmap = {nums[-1]: nums[-1]}

        for i in range(len(nums) - 2, -1, -1):
            hashmap[nums[i]] = nums[i] + nums[i+1]
            nums[i] += nums[i+1]

        def toGreater(node):
            if not node:
                return 

            toGreater(node.left)
            toGreater(node.right)
            node.val = hashmap[node.val]


        toGreater(root)
        return root


class CleanerSolution: #Same complexity as above
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        def dfs(node):
            nonlocal curSum

            if not node:
                return 

            dfs(node.right)
            tmp = node.val
            node.val += curSum
            curSum += tmp
            dfs(node.left)


        dfs(root)
        return root

            
        
