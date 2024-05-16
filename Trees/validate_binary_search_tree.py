# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, low, high):
            if not root:
                return True

            if not (low < root.val < high):
                return False

            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high) #on the left side you want every value to less than the root, on the right side you want every value to be greater than the root


        return isValid(root, -math.inf, math.inf)




        
