"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1085966067/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1: #Time complexity O(nlogn) due to slicing, Space complexity O(n)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums)//2
        node = TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))
        return node
    

class Solution2: #Time complexity O(n), Space complexity O(n)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None

            m = (l+r)//2
            root = TreeNode(nums[m], helper(l, m-1), helper(m+1, r))
            return root

        return helper(0, len(nums)-1)
