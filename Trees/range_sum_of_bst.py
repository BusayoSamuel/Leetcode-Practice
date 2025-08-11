# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low or root.val > high:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


class BetterSolution: #Time complexity O(n) , Space complexity O(n) but if tree is balanced O(logn) in each case
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high) #we go right because the tree is a BST so can assume all values to the left would be less than low as well
        if root.val > high:
            return self.rangeSumBST(root.left, low, high) #we go left because the tree is a BST so can assume all values to the right would be greater than high as well

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


class MySolution: #Not as efficient, but same complexity as above
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)

        if low <= root.val <= high:
            return root.val + left + right
        else:
            return left + right
        
