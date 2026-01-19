"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n) because at most we visit each node twice (for traversing and reversing), Space complexity O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []

        if not root:
            return None

        q.append(root)
        level = 1

        while q:
            nodes = []
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                nodes.append(node.val)

            if level % 2 != 0:
                res.append(nodes)
            else:
                res.append(nodes[::-1])
            
            level += 1

        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CleanerSolution: #Same complexity
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root] if root else [])

        while q:
            level = []
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node.val)

            level = level[::-1] if len(res) % 2 else level #the len of res tells us what level we're on
            res.append(level)

        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MyOtherSolution: #Same complexity as above
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque([root] if root else [])
        left = True

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

                level.append(node.val)

            if left:
                res.append(level)
            else:
                res.append(level[::-1])

            left = not left


        return res

        
                



        
