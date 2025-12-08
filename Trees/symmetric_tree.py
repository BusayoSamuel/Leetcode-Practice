"""
https://leetcode.com/problems/symmetric-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecoursiveSolution: #Time complexity O(n), Space complexity O(logn)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right

        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(left, right)
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class IterativeSolution: #Time complexity O(n), Space complexity O(1)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        qright = deque()
        qleft = deque()

        qright.append(root.right)
        qleft.append(root.left)

        while qright and qleft:
            nodeLeft = qleft.pop()
            nodeRight = qright.pop()

            if not nodeLeft and not nodeRight:
                continue

            if not nodeLeft or not nodeRight or nodeLeft.val != nodeRight.val:
                return False

            qleft.append(nodeLeft.right)
            qleft.append(nodeLeft.left)

            qright.append(nodeRight.left)
            qright.append(nodeRight.right)

        return not qright and not qleft


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(logn)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)


        return dfs(root.left, root.right)

