"""
https://leetcode.com/problems/binary-tree-right-side-view/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        if not root:
            return res

        q.append(root)
        
        while q:
            curLen = len(q)

            for i in range(curLen):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if i == curLen - 1:
                    res.append(node.val)

        return res