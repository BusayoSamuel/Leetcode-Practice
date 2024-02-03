"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        notVisited = deque()
        
        if root:
            notVisited.append(root)

        while notVisited:
            level = []
            for i in range(len(notVisited)):
                curNode = notVisited.popleft()

                if curNode.left:
                    notVisited.append(curNode.left)

                if curNode.right:
                    notVisited.append(curNode.right)

                level.append(curNode.val)

            res.append(level)

        return res

            
        
