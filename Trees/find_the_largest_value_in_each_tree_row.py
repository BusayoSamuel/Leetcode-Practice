"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        if root:
            q.append(root)

        res = []

        while q:
            cur = -math.inf #or q[0].val
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                cur = max(cur, node.val)
            res.append(cur)

        return res
            
        
