"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        q.append(root)
        xCount = 1

        while q:
            level = []
            prevNode = TreeNode()

            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    if node.right and not node.left:
                        return False

                    if node.left and not prevNode:
                        return False

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

                    level.append(node) 
                    prevNode = node.right

            if len(level) != xCount and q:
                return False

            xCount *= 2

        return True                
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CleanerSolution: #Same complexity
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        q.append(root)
        foundNone = False

        while q:

            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    if foundNone: #Upon the first encounter with a null node, you expect every other node after to be null else it is not complete
                        return False
                    
                    q.append(node.left)
                    q.append(node.right)
                    
                else:
                    foundNone = True 

        return True     