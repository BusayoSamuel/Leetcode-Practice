"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 1
        level = 0
        maxV = -math.inf

        while q:
            total = 0
            level += 1
            for i in range(len(q)):
                node = q.popleft()

                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if not res or total > maxV:
                res = level
                maxV = total

        return res



        
