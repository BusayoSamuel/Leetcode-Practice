"""
https://leetcode.com/problems/move-zeroes/description/
"""

class Solution: #Time complexity O(n), #Space complexity O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 #left pointer is used to keep track of where the next none-zero number should go
        
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

            